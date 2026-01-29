"""
User service
"""

from uuid import UUID

from src.model.user import User
from src.repository import user_repository


async def retrieve_users() -> [User]:
    """
    Retrieve all users
    """

    return user_repository.find()


async def retrieve_user_by_id(id_: str) -> User | None:
    """
    Retrieve user by id
    """

    return user_repository.find_one(UUID(str(id_), version=4))


async def create_user(user: User) -> User | None:
    """
    Create user
    """

    return user_repository.create(user)
