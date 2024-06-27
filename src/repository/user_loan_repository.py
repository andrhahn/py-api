"""
UserLoan repository
"""

from sqlmodel import select
from src.service import database_service
from src.model.user_loan import UserLoan


def find() -> [UserLoan]:
    """
    Retrieve all user loans
    """

    with database_service.get_session() as session:
        statement = select(UserLoan)

        results = session.exec(statement)

        return results.all()


def find_one(id_: str) -> UserLoan | None:
    """
    Retrieve user loan by id
    """

    with database_service.get_session() as session:
        return session.get(UserLoan, id_)


def find_one_by_user_id(user_id: str) -> UserLoan | None:
    """
    Retrieve user loan by user id
    """

    with database_service.get_session() as session:
        return session.get(UserLoan, user_id)


def create(user_loan: UserLoan) -> UserLoan:
    """
    Create user loan
    """

    with database_service.get_session() as session:
        session.add(user_loan)

        session.commit()

        session.refresh(user_loan)

        return user_loan
