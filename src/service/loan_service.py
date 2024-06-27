"""
Loan service
"""

from src.model.loan import Loan, LoanSchedule, LoanSummary
from src.repository import loan_repository


async def retrieve_loans(user_id: str) -> [Loan]:
    """
    Retrieve all loans, optional user_id param
    """

    return loan_repository.find_one_by_user_id(user_id)


async def retrieve_loan_by_id(id_: str) -> Loan | None:
    """
    Retrieve loan by id
    """

    return loan_repository.find_one(id_)


async def retrieve_loan_schedule(id_: str) -> LoanSchedule | None:
    """
    Retrieve loan schedule
    """

    if id_:
        print("Placeholder...")

    return None  # TODO...


async def retrieve_loan_summary(id_: str) -> LoanSummary | None:
    """
    Retrieve loan summary
    """

    if id_:
        print("Placeholder...")

    return None  # TODO...


async def create_loan(loan: Loan) -> Loan | None:
    """
    Create loan
    """

    return loan_repository.create(loan)
