"""
UserLoan repository tests
"""

from uuid import uuid4
import pytest
from src.model.user_loan import UserLoan
from src.repository import user_loan_repository
from src.service import database_service


@pytest.fixture(autouse=True, name="user_loans")
def fixture_user_loans():
    """
    User loans mock fixture
    """

    database_service.init()

    user1_id = uuid4()
    user2_id = uuid4()

    loan1_id = uuid4()
    loan2_id = uuid4()

    user_loans = [
        user_loan_repository.create(UserLoan(uuid4(), user1_id, loan1_id, True)),
        user_loan_repository.create(UserLoan(uuid4(), user1_id, loan2_id, True)),
        user_loan_repository.create(UserLoan(uuid4(), user2_id, loan2_id, False)),
    ]

    yield user_loans


@pytest.mark.asyncio
async def test_find(user_loans):
    """
    Find test
    """

    result = user_loan_repository.find()

    assert len(result) == len(user_loans)


@pytest.mark.asyncio
async def test_find_one(user_loans):
    """
    Find one test
    """

    result = user_loan_repository.find_one(user_loans[0].id)

    assert result.id == user_loans[0].id


@pytest.mark.asyncio
async def test_find_one_not_found():
    """
    Find one not found test
    """

    result = user_loan_repository.find_one(uuid4())

    assert result is None


@pytest.mark.asyncio
async def test_find_by_user_id(user_loans):
    """
    Find by user id test
    """

    result = user_loan_repository.find_by_user_id(user_loans[0].user_id)

    assert len(result) == 2
    assert result[0].user_id == user_loans[0].user_id


@pytest.mark.asyncio
async def test_find_by_user_id_not_found():
    """
    Find by user id not found test
    """

    result = user_loan_repository.find_by_user_id(uuid4())

    assert result == []


@pytest.mark.asyncio
async def test_create_user_loan():
    """
    Create user loan test
    """

    user_loan = UserLoan(uuid4(), uuid4(), uuid4(), True)

    result = user_loan_repository.create(user_loan)

    assert result.user_id == user_loan.user_id
    assert result.loan_id == user_loan.loan_id
