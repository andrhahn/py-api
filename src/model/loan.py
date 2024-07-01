"""
Loan models
"""

from uuid import UUID, uuid4
from typing import Optional
from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class Loan(SQLModel, table=True):
    """
    Loan model
    """

    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    amount: float = Field(gt=0)
    annual_interest_rate: float = Field(gt=0)
    loan_term: int = Field(gt=0, le=60)

    def __init__(self, _id, amount, annual_interest_rate, loan_term):
        super().__init__(
            amount=amount,
            annual_interest_rate=annual_interest_rate,
            loan_term=loan_term,
        )


class LoanSchedule(BaseModel):
    """
    LoanSchedule model
    """

    month: int = Field(gt=0, le=60)
    remaining_balance: float = Field(ge=0)
    monthly_payment: float = Field(gt=0)

    def __init__(self, _id, month, remaining_balance, monthly_payment):
        super().__init__(
            month=month,
            remaining_balance=remaining_balance,
            monthly_payment=monthly_payment,
        )


class LoanSummary(BaseModel):
    """
    LoanSummary model
    """

    principle_balance: float = Field(ge=0)
    principle_paid: float = Field(ge=0)
    interest_paid: float = Field(ge=0)

    def __init__(self, _id, principle_balance, principle_paid, interest_paid):
        super().__init__(
            principle_balance=principle_balance,
            principle_paid=principle_paid,
            interest_paid=interest_paid,
        )


class CreateLoanRequest(BaseModel):
    """
    CreateLoanRequest model
    """

    user_id: UUID = Field()
    amount: float = Field(gt=0)
    annual_interest_rate: float = Field(gt=0)
    loan_term: int = Field(gt=0, le=60)

    def __init__(self, user_id, amount, annual_interest_rate, loan_term):
        super().__init__(
            user_id=user_id,
            amount=amount,
            annual_interest_rate=annual_interest_rate,
            loan_term=loan_term,
        )


class ShareLoanRequest(BaseModel):
    """
    ShareLoanRequest model
    """

    loan_id: UUID = Field()
    user_id: UUID = Field()

    def __init__(self, loan_id, user_id):
        super().__init__(
            loan_id=loan_id,
            user_id=user_id,
        )


class AmortizationSchedule(BaseModel):
    """
    AmortizationSchedule model
    """

    month: int = Field(gt=0, le=60)
    amount: float = Field(gt=0)
    interest: float = Field(gt=0)
    principle: float = Field(gt=0)
    balance: float = Field(ge=0)

    def __init__(self, _id, month, amount, interest, principle, balance):
        super().__init__(
            month=month,
            amount=amount,
            interest=interest,
            principle=principle,
            balance=balance,
        )
