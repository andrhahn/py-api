"""
User route tests
"""

from uuid import uuid4
from datetime import datetime, timezone
from unittest.mock import AsyncMock
from pydantic import ValidationError
from fastapi.exceptions import HTTPException
import pytest
from callee import Attrs
from src.model.user import User, CreateUserRequest
from src.router import user_route


now = datetime.now(timezone.utc)

users = [
    User(uuid4(), "Andy Test", now),
    User(uuid4(), "Sam Test", now),
    User(uuid4(), "Leela Test", now),
]


@pytest.fixture(name="mock_retrieve_users")
def fixture_mock_retrieve_users(mocker):
    """
    Retrieve users mock fixture
    """
    async_mock = AsyncMock()
    mocker.patch("src.service.user_service.retrieve_users", side_effect=async_mock)
    return async_mock


@pytest.fixture(name="mock_retrieve_user_by_id")
def fixture_mock_retrieve_user_by_id(mocker):
    """
    Retrieve user by id mock fixture
    """
    async_mock = AsyncMock()
    mocker.patch("src.service.user_service.retrieve_user_by_id", side_effect=async_mock)
    return async_mock


@pytest.fixture(name="mock_create_user")
def fixture_mock_create_user(mocker):
    """
    Create user mock fixture
    """
    async_mock = AsyncMock()
    mocker.patch("src.service.user_service.create_user", side_effect=async_mock)
    return async_mock


@pytest.mark.asyncio
async def test_get_users(mock_retrieve_users):
    """
    Get users test
    """
    mock_retrieve_users.return_value = users

    result = await user_route.get_users()

    assert result == users


@pytest.mark.asyncio
async def test_get_users_not_found(mock_retrieve_users):
    """
    Get users not found test
    """
    mock_retrieve_users.return_value = []

    result = await user_route.get_users()

    assert result == []


@pytest.mark.asyncio
async def test_get_user_by_id(mock_retrieve_user_by_id):
    """
    Get user by id test
    """
    mock_retrieve_user_by_id.return_value = users[0]

    result = await user_route.get_user_by_id(str(users[0].id))

    mock_retrieve_user_by_id.assert_called_with(str(users[0].id))

    assert result == users[0]


@pytest.mark.asyncio
async def test_get_user_by_id_not_found(mock_retrieve_user_by_id):
    """
    Get user by id not found test
    """
    mock_retrieve_user_by_id.return_value = None

    try:
        await user_route.get_user_by_id(str(users[0].id))
    except HTTPException as e:
        assert e.status_code == 404
        assert e.detail == "User not found"

        mock_retrieve_user_by_id.assert_called_with(str(users[0].id))
    else:
        raise pytest.fail("Test failed due to error not being caught")


@pytest.mark.asyncio
async def test_create_user(mock_create_user):
    """
    Create user test
    """
    mock_create_user.return_value = users[1]

    result = await user_route.create_user(
        CreateUserRequest(users[1].name, users[1].signup_date)
    )

    mock_create_user.assert_called_once()

    mock_create_user.assert_called_once_with(
        Attrs(name=users[1].name, signup_date=users[1].signup_date)
    )

    assert result == users[1]


@pytest.mark.asyncio
async def test_create_user_missing_name(mock_create_user):
    """
    Create user missing name test
    """
    mock_create_user.return_value = users[1]

    try:
        await user_route.create_user(CreateUserRequest(None, users[1].signup_date))
    except ValidationError as e:
        errors = e.errors()
        assert len(errors) == 1
        assert errors[0]["msg"] == "Input should be a valid string"

        mock_create_user.assert_not_called()
    else:
        raise pytest.fail("Test failed due to error not being caught")


@pytest.mark.asyncio
async def test_create_user_invalid_signup_date(mock_create_user):
    """
    Create user missing name test
    """
    mock_create_user.return_value = users[1]

    try:
        await user_route.create_user(CreateUserRequest(users[1].name, "foo"))
    except ValidationError as e:
        errors = e.errors()
        assert len(errors) == 1
        assert (
            errors[0]["msg"]
            == "Input should be a valid datetime or date, input is too short"
        )

        mock_create_user.assert_not_called()
    else:
        raise pytest.fail("Test failed due to error not being caught")
