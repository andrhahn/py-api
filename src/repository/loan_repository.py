"""
Loan repository
"""

from sqlmodel import select, col
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


def find_by_ids(ids: [str]) -> [Loan]:
    """
    Retrieve loans by ids
    """

    with database_service.get_session() as session:
        statement = select(Loan).where(col(Loan.id).in_(ids))

        results = session.exec(statement)

        return results.all()


def create(loan: Loan) -> Loan:
    """
    Create loan
    """

    with database_service.get_session() as session:
        session.add(loan)

        session.commit()

        session.refresh(loan)

        return loan
