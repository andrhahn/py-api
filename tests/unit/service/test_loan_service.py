"""
Loan service tests
"""

from uuid import uuid4
from unittest.mock import AsyncMock
import pytest
from src.model.loan import Loan
from src.service import loan_service


@pytest.fixture(name="mock_retrieve_loan_by_id")
def fixture_retrieve_loan_by_id(mocker):
    """
    Retrieve loan by id mock fixture
    """

    async_mock = AsyncMock()
    mocker.patch("src.service.loan_service.retrieve_loan_by_id", side_effect=async_mock)
    return async_mock


@pytest.mark.asyncio
async def test_retrieve_loan_schedule(mock_retrieve_loan_by_id):
    """
    Retrieve loan schedule test
    """

    loan = Loan(uuid4(), 1000, 0.1, 6)

    mock_retrieve_loan_by_id.return_value = loan

    result = await loan_service.retrieve_loan_schedule(str(loan.id))

    print(result)

    assert len(result) == 6
    assert result[0].month == 1
    assert result[0].remaining_balance == 836.77
    assert result[0].monthly_payment == 171.56

    assert result[1].month == 2
    assert result[1].remaining_balance == 672.18
    assert result[1].monthly_payment == 171.56

    assert result[2].month == 3
    assert result[2].remaining_balance == 506.22
    assert result[2].monthly_payment == 171.56

    assert result[3].month == 4
    assert result[3].remaining_balance == 338.88
    assert result[3].monthly_payment == 171.56

    assert result[4].month == 5
    assert result[4].remaining_balance == 170.14
    assert result[4].monthly_payment == 171.56

    assert result[5].month == 6
    assert result[5].remaining_balance == 0
    assert result[5].monthly_payment == 171.56
