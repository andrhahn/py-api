"""
Loan service
"""

from uuid import UUID

from src.model.loan import Loan, AmortizationSchedule, LoanSchedule, LoanSummary
from src.repository import loan_repository
from src.service import user_loan_service
from src.model.user_loan import UserLoan


async def retrieve_loans() -> [Loan]:
    """
    Retrieve all loans
    """

    return loan_repository.find()


async def retrieve_loans_by_user_id(user_id: str) -> [Loan]:
    """
    Retrieve all loans by user id
    """

    user_loans = await user_loan_service.retrieve_user_loans_by_user_id(
        UUID(str(user_id), version=4)
    )

    return loan_repository.find_by_ids([user_loan.loan_id for user_loan in user_loans])


async def retrieve_loan_by_id(id_: str) -> Loan | None:
    """
    Retrieve loan by id
    """

    return loan_repository.find_one(UUID(str(id_), version=4))


async def retrieve_loan_schedule(id_: str) -> [LoanSchedule]:
    """
    Retrieve loan schedule
    """

    result = []

    loan = await retrieve_loan_by_id(id_)

    if loan:
        amortization_schedule = await calculate_amortization_schedule(
            loan.amount, loan.annual_interest_rate, loan.loan_term
        )

        for item in amortization_schedule:
            result.append(
                LoanSchedule(
                    None, item.month, f"{item.balance:.2f}", f"{item.amount:.2f}"
                )
            )

    return result


async def retrieve_loan_summary(id_: str, month: int) -> LoanSummary | None:
    """
    Retrieve loan summary
    """

    result = None

    loan = await retrieve_loan_by_id(id_)

    if loan:
        amortization_schedule = await calculate_amortization_schedule(
            loan.amount, loan.annual_interest_rate, loan.loan_term
        )

        principle_balance = 0
        interest_paid = 0
        principle_paid = 0

        for i in amortization_schedule:
            if i.month <= month:
                interest_paid += i.interest
                principle_paid += i.principle

                if i.month == month:
                    principle_balance = i.balance

        result = LoanSummary(
            id_,
            round(principle_balance, 2),
            round(principle_paid, 2),
            round(interest_paid, 2),
        )

    return result


async def create_loan(loan: Loan, user_id) -> Loan | None:
    """
    Create loan
    """

    loan = loan_repository.create(loan)

    await user_loan_service.create_user_loan(UserLoan(None, user_id, loan.id, True))

    return loan


async def share_loan(user_id, loan_id) -> Loan | None:
    """
    Share loan
    """

    await user_loan_service.create_user_loan(UserLoan(None, user_id, loan_id, False))

    return await retrieve_loan_by_id(loan_id)


async def calculate_amortization_schedule(
    amount_: float, annual_interest_rate_: float, loan_term_: int
) -> [AmortizationSchedule]:
    """
    Calculate loan amortization schedule
    """

    result = []

    monthly_interest_rate = annual_interest_rate_ / 100 / 12

    total_payments = loan_term_

    monthly_payment = (
        amount_
        * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments)
        / ((1 + monthly_interest_rate) ** total_payments - 1)
    )

    principal_remaining = amount_

    for payment_number in range(1, total_payments + 1):
        interest_payment = principal_remaining * monthly_interest_rate

        if payment_number == total_payments:
            principal_payment = principal_remaining
        else:
            principal_payment = monthly_payment - interest_payment

        principal_remaining -= principal_payment

        result.append(
            AmortizationSchedule(
                None,
                payment_number,
                round(monthly_payment, 2),
                round(interest_payment, 6),
                round(principal_payment, 2),
                round(principal_remaining, 2),
            )
        )

    return result
