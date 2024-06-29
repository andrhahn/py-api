"""
Loan service
"""

from amortization.schedule import amortization_schedule
from src.model.loan import Loan, LoanSchedule, LoanSummary
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

    loan = await retrieve_loan_by_id(id_)

    result = []

    if loan:
        # pylint: disable=unused-variable
        for number, amount, interest, principal, balance in amortization_schedule(
            loan.amount, loan.annual_interest_rate, loan.loan_term
        ):
            result.append(
                LoanSchedule(
                    None, number, f"{balance:.2f}", f"{amount:.2f}"
                )
            )

    return result


async def retrieve_loan_summary(id_: str, month: int) -> LoanSummary | None:
    """
    Retrieve loan summary
    """

    print(month)

    return LoanSummary(id_, 100, 200, 100)


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
