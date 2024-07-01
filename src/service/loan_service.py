"""
Loan service
"""

from amortization.schedule import amortization_schedule as amort_sched
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

    user_loans = await user_loan_service.retrieve_user_loans_by_user_id(user_id)

    return loan_repository.find_by_ids([user_loan.loan_id for user_loan in user_loans])


async def retrieve_loan_by_id(id_: str) -> Loan | None:
    """
    Retrieve loan by id
    """

    return loan_repository.find_one(id_)


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

        print(amortization_schedule)

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
            f"{principle_balance:.2f}",
            f"{principle_paid:.2f}",
            f"{interest_paid:.2f}",
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

    for number, amount, interest, principal, balance in amort_sched(
        amount_, annual_interest_rate_, loan_term_
    ):
        result.append(
            AmortizationSchedule(None, number, amount, interest, principal, balance)
        )

    return result
