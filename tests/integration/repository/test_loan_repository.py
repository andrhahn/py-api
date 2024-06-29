"""
Loan repository tests
"""

from uuid import uuid4
import pytest
from src.model.loan import Loan
from src.repository import loan_repository
from src.service import database_service


@pytest.fixture(autouse=True, name="loans")
def fixture_loans():
    """
    Loans mock fixture
    """

    database_service.init()

    loans = [
        loan_repository.create(Loan(uuid4(), 1000.00, 19.99, 36)),
        loan_repository.create(Loan(uuid4(), 750.00, 17.75, 30)),
        loan_repository.create(Loan(uuid4(), 500.00, 15.5, 24)),
        loan_repository.create(Loan(uuid4(), 20.00, 1.99, 6)),
    ]

    yield loans


@pytest.mark.asyncio
async def test_find(loans):
    """
    Find test
    """

    result = loan_repository.find()

    assert len(result) == len(loans)


@pytest.mark.asyncio
async def test_find_one(loans):
    """
    Find one test
    """

    result = loan_repository.find_one(str(loans[0].id))

    assert result.amount == loans[0].amount


@pytest.mark.asyncio
async def test_find_one_not_found():
    """
    Find one not found test
    """

    result = loan_repository.find_one(str(uuid4()))

    assert result is None


@pytest.mark.asyncio
async def test_find_by_ids(loans):
    """
    Find by ids test
    """

    result = loan_repository.find_by_ids([loans[0].id, loans[1].id])

    assert len(result) == 2


@pytest.mark.asyncio
async def test_find_one_by_user_ids_not_found():
    """
    Find by ids not found test
    """

    result = loan_repository.find_by_ids([uuid4(), uuid4()])

    assert result == []


@pytest.mark.asyncio
async def test_create_loan():
    """
    Create loan test
    """

    loan = Loan(uuid4(), 50.00, 19.99, 36)

    result = loan_repository.create(loan)

    assert result.id == loan.id
