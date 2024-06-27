"""
Loan repository
"""

from sqlmodel import select
from src.service import database_service
from src.model.loan import Loan


def find() -> [Loan]:
    """
    Retrieve all loans
    """

    with database_service.get_session() as session:
        statement = select(Loan)

        results = session.exec(statement)

        return results.all()


def find_one(id_: str) -> Loan | None:
    """
    Retrieve loan by id
    """

    with database_service.get_session() as session:
        return session.get(Loan, id_)


def find_one_by_user_id(user_id: str) -> Loan | None:
    """
    Retrieve loan by user id
    """

    with database_service.get_session() as session:
        return session.get(Loan, user_id)


def create(loan: Loan) -> Loan:
    """
    Create loan
    """

    with database_service.get_session() as session:
        session.add(loan)

        session.commit()

        session.refresh(loan)

        return loan
