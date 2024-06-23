"""
Loan models
"""

from uuid import UUID, uuid4
from typing import List, Optional
from pydantic import BaseModel, Field


class Loan(BaseModel):
    """
    Loan model
    """

    id: UUID | None = Field(default_factory=uuid4)
    user_id: UUID
    shared_user_ids: Optional[List[UUID]] = None
    amount: float = Field(gt=0)
    annual_interest_rate: float = Field(gt=0)
    loan_term: int = Field(gt=0, le=60)

    def __init__(
        self, _id, user_id, shared_user_ids, amount, annual_interest_rate, loan_term
    ):
        super().__init__(
            user_id=user_id,
            shared_user_ids=shared_user_ids,
            amount=amount,
            annual_interest_rate=annual_interest_rate,
            loan_term=loan_term,
        )


class LoanSchedule(BaseModel):
    """
    LoanSchedule model
    """

    month: int = Field(gt=0, le=12)
    remaining_balance: float = Field(gt=0)
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

    principle_balance: float = Field(gt=0)
    principle_paid: float = Field(gt=0)
    interest_paid: float = Field(gt=0)

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
    shared_user_ids: Optional[List[UUID]] = Field(min_length=0, max_length=10)
    amount: float = Field(gt=0)
    annual_interest_rate: float = Field(gt=0)
    loan_term: int = Field(gt=0, le=60)

    def __init__(
        self, user_id, shared_user_ids, amount, annual_interest_rate, loan_term
    ):
        super().__init__(
            user_id=user_id,
            shared_user_ids=shared_user_ids,
            amount=amount,
            annual_interest_rate=annual_interest_rate,
            loan_term=loan_term,
        )
