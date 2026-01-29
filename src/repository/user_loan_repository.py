"""
UserLoan repository
"""

from uuid import UUID

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


def find_one(id_: UUID) -> UserLoan | None:
    """
    Retrieve user loan by id
    """

    with database_service.get_session() as session:
        return session.get(UserLoan, id_)


def find_by_user_id(user_id: UUID) -> [UserLoan]:
    """
    Retrieve all user loans by user id
    """

    with database_service.get_session() as session:
        statement = select(UserLoan).where(UserLoan.user_id == user_id)

        results = session.exec(statement)

        return results.all()


def create(user_loan: UserLoan) -> UserLoan:
    """
    Create user loan
    """

    with database_service.get_session() as session:
        session.add(user_loan)

        session.commit()

        session.refresh(user_loan)

        return user_loan
