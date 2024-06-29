"""
UserLoan repository tests
"""

from uuid import uuid4
from sqlmodel import SQLModel
import pytest
from src.model.user_loan import UserLoan
from src.repository import user_loan_repository
from src.service import database_service


@pytest.fixture(autouse=True, name="user_loans")
def fixture_user_loans():
    """
    User loans mock fixture
    """

    print("setup")

    SQLModel.metadata.create_all(database_service.engine)

    user1_id = uuid4()
    user2_id = uuid4()

    loan1_id = uuid4()
    loan2_id = uuid4()

    user_loans = [
        user_loan_repository.create(UserLoan(uuid4(), user1_id, loan1_id, True)),
        user_loan_repository.create(UserLoan(uuid4(), user2_id, loan2_id, True)),
        user_loan_repository.create(UserLoan(uuid4(), user2_id, loan1_id, False)),
    ]

    yield user_loans

    print("teardown")

    SQLModel.metadata.drop_all(database_service.engine)


@pytest.mark.asyncio
async def test_get_user_loans(user_loans):
    """
    Get user loans test
    """

    result = user_loan_repository.find()

    assert len(result) == len(user_loans)


@pytest.mark.asyncio
async def test_get_user_loan_by_id(user_loans):
    """
    Get user loan by id test
    """

    result = user_loan_repository.find_one(str(user_loans[0].id))

    assert result.id == user_loans[0].id


@pytest.mark.asyncio
async def test_get_user_loan_by_id_not_found():
    """
    Get user loan by id not found test
    """

    result = user_loan_repository.find_one(str(uuid4()))

    assert result is None


@pytest.mark.asyncio
async def test_create_user_loan():
    """
    Create user loan test
    """

    user_loan = UserLoan(uuid4(), uuid4(), uuid4(), True)

    result = user_loan_repository.create(user_loan)

    assert result.user_id == user_loan.user_id
    assert result.loan_id == user_loan.loan_id
