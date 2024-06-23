"""
User service
"""

from datetime import datetime, timezone
from uuid import uuid4
from src.model.user import User


now = datetime.now(timezone.utc)

users = [
    User(uuid4(), "Andy", now),
    User(uuid4(), "Sam", now),
    User(uuid4(), "Leela", now),
]


async def retrieve_users() -> [User]:
    """
    Retrieve all users
    """
    return users


async def retrieve_user_by_id(id_: str) -> User | None:
    """
    Retrieve user by id
    """
    user: User | None = None

    if id_ == str(users[0].id):
        user = users[0]
    elif id_ == str(users[1].id):
        user = users[1]
    elif id_ == str(users[2].id):
        user = users[2]

    return user


async def create_user(user: User) -> User | None:
    """
    Create user
    """
    user.id = uuid4()

    users.append(user)

    return user
