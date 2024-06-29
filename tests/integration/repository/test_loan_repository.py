"""
Loan repository tests
"""

from uuid import uuid4
from sqlmodel import SQLModel
import pytest
from src.model.loan import Loan
from src.repository import loan_repository
from src.service import database_service


@pytest.fixture(autouse=True, name="loans")
def fixture_loans():
    """
    Loans mock fixture
    """

    print("setup")

    SQLModel.metadata.create_all(database_service.engine)

    loans = [
        loan_repository.create(Loan(uuid4(), uuid4(), 1000.00, 19.99, 36)),
        loan_repository.create(Loan(uuid4(), uuid4(), 750.00, 17.75, 30)),
        loan_repository.create(Loan(uuid4(), uuid4(), 500.00, 15.5, 24)),
        loan_repository.create(Loan(uuid4(), uuid4(), 20.00, 1.99, 6)),
    ]

    yield loans

    print("teardown")

    SQLModel.metadata.drop_all(database_service.engine)


@pytest.mark.asyncio
async def test_get_loans(loans):
    """
    Get loans test
    """

    result = loan_repository.find()

    assert len(result) == len(loans)


@pytest.mark.asyncio
async def test_get_loan_by_id(loans):
    """
    Get loan by id test
    """

    result = loan_repository.find_one(str(loans[0].id))

    assert result.amount == loans[0].amount


@pytest.mark.asyncio
async def test_get_loan_by_id_not_found():
    """
    Get loan by id not found test
    """

    result = loan_repository.find_one(str(uuid4()))

    assert result is None


@pytest.mark.asyncio
async def test_create_loan():
    """
    Create loan test
    """

    loan = Loan(uuid4(), uuid4(), 50.00, 19.99, 36)

    result = loan_repository.create(loan)

    assert result.id == loan.id
