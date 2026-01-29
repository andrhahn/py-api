"""
User repository tests
"""

from uuid import uuid4
from datetime import datetime, timezone
import pytest
from src.model.user import User
from src.repository import user_repository
from src.service import database_service


@pytest.fixture(autouse=True, name="users")
def fixture_users():
    """
    Users mock fixture
    """

    database_service.init()

    now = datetime.now(timezone.utc)

    users = [
        user_repository.create(User(uuid4(), "Andy Test", now)),
        user_repository.create(User(uuid4(), "Sam Test", now)),
        user_repository.create(User(uuid4(), "Leela Test", now)),
    ]

    yield users


@pytest.mark.asyncio
async def test_find(users):
    """
    Find test
    """

    result = user_repository.find()

    assert len(result) == len(users)


@pytest.mark.asyncio
async def test_find_one(users):
    """
    Find one test
    """

    result = user_repository.find_one(users[0].id)

    assert result.name == users[0].name


@pytest.mark.asyncio
async def test_find_one_not_found():
    """
    Find one not found test
    """

    result = user_repository.find_one(uuid4())

    assert result is None


@pytest.mark.asyncio
async def test_create_user():
    """
    Create user test
    """

    user = User(uuid4(), "Kelsey Test", datetime.now(timezone.utc))

    result = user_repository.create(user)

    assert result.name == user.name
