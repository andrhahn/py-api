"""
User repository
"""

from uuid import UUID

from sqlmodel import select
from src.service import database_service
from src.model.user import User


def find() -> [User]:
    """
    Retrieve all users
    """

    with database_service.get_session() as session:
        statement = select(User)

        results = session.exec(statement)

        return results.all()


def find_one(id_: UUID) -> User | None:
    """
    Retrieve user by id
    """

    with database_service.get_session() as session:
        return session.get(User, id_)


def create(user: User) -> User:
    """
    Create user
    """

    with database_service.get_session() as session:
        session.add(user)

        session.commit()

        session.refresh(user)

        return user
