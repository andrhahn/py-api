"""
User repository tests
"""

from uuid import uuid4
from datetime import datetime, timezone
from sqlmodel import SQLModel
import pytest
from src.model.user import User
from src.repository import user_repository
from src.service import database_service


@pytest.fixture(autouse=True, name="users")
def fixture_users():
    """
   Users mock fixture
   """

    print("setup")

    SQLModel.metadata.create_all(database_service.engine)

    now = datetime.now(timezone.utc)

    users = [
        user_repository.create(User(uuid4(), "Andy Test", now)),
        user_repository.create(User(uuid4(), "Sam Test", now)),
        user_repository.create(User(uuid4(), "Leela Test", now)),
    ]

    yield users

    print("teardown")

    SQLModel.metadata.drop_all(database_service.engine)


@pytest.mark.asyncio
async def test_get_users(users):
    """
    Get users test
    """

    result = user_repository.find()

    assert len(result) == len(users)


@pytest.mark.asyncio
async def test_get_user_by_id(users):
    """
    Get user by id test
    """

    result = user_repository.find_one(str(users[0].id))

    assert result.name == users[0].name


@pytest.mark.asyncio
async def test_get_user_by_id_not_found():
    """
    Get user by id not found test
    """

    result = user_repository.find_one(str(uuid4()))

    assert result is None


@pytest.mark.asyncio
async def test_create_user():
    """
    Create user test
    """

    user = User(uuid4(), "Kelsey Test", datetime.now(timezone.utc))

    result = user_repository.create(user)

    assert result.name == user.name
