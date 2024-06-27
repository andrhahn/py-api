"""
UserLoan service
"""

from src.model.user_loan import UserLoan
from src.repository import user_loan_repository


async def retrieve_user_loans_by_user_id(user_id: str) -> [UserLoan]:
    """
    Retrieve user loans by user id
    """

    return user_loan_repository.find_one_by_user_id(user_id)


async def create_user_loan(user_loan: UserLoan) -> UserLoan | None:
    """
    Create user loan
    """

    return user_loan_repository.create(user_loan)
