"""
Loan route tests
"""

from uuid import uuid4
from unittest.mock import AsyncMock
from pydantic import ValidationError
from fastapi.exceptions import HTTPException
import pytest
from callee import Attrs
from src.model.loan import Loan, LoanSchedule, LoanSummary, CreateLoanRequest
from src.router import loan_route


loans = [
    Loan(uuid4(), 1000.00, 19.99, 36),
    Loan(uuid4(), 750.00, 17.75, 30),
    Loan(uuid4(), 500.00, 15.5, 24),
    Loan(uuid4(), 20.00, 1.99, 6),
]

loans_schedules = [
    LoanSchedule(None, 5, 750.00, 200.00),
    LoanSchedule(None, 5, 500.00, 150.00),
    LoanSchedule(None, 5, 250.00, 100.00),
    LoanSchedule(None, 5, 5.00, 15.00),
]

loans_summaries = [
    LoanSummary(None, 225.00, 200.00, 200.00),
    LoanSummary(None, 220.00, 200.00, 100.00),
    LoanSummary(None, 225.00, 200.00, 50.00),
    LoanSummary(None, 12.00, 10.00, 5.00),
]


@pytest.fixture(name="mock_retrieve_loans")
def fixture_mock_retrieve_loans(mocker):
    """
    Get loans mock fixture
    """
    async_mock = AsyncMock()
    mocker.patch("src.service.loan_service.retrieve_loans", side_effect=async_mock)
    return async_mock


@pytest.fixture(name="mock_retrieve_loans_by_user_id")
def fixture_mock_retrieve_loans_by_user_id(mocker):
    """
    Get loans mock fixture
    """
    async_mock = AsyncMock()
    mocker.patch(
        "src.service.loan_service.retrieve_loans_by_user_id", side_effect=async_mock
    )
    return async_mock


@pytest.fixture(name="mock_retrieve_loan_by_id")
def fixture_mock_retrieve_loan_by_id(mocker):
    """
    Get loan by id mock fixture
    """
    async_mock = AsyncMock()
    mocker.patch("src.service.loan_service.retrieve_loan_by_id", side_effect=async_mock)
    return async_mock


@pytest.fixture(name="mock_retrieve_loan_schedule")
def fixture_mock_retrieve_loan_schedule(mocker):
    """
    Get loan schedule mock fixture
    """
    async_mock = AsyncMock()
    mocker.patch(
        "src.service.loan_service.retrieve_loan_schedule", side_effect=async_mock
    )
    return async_mock


@pytest.fixture(name="mock_retrieve_loan_summary")
def fixture_mock_retrieve_loan_summary(mocker):
    """
    Get loan summary mock fixture
    """
    async_mock = AsyncMock()
    mocker.patch(
        "src.service.loan_service.retrieve_loan_summary", side_effect=async_mock
    )
    return async_mock


@pytest.fixture(name="mock_create_loan")
def fixture_mock_create_loan(mocker):
    """
    Create loan mock fixture
    """
    async_mock = AsyncMock()
    mocker.patch("src.service.loan_service.create_loan", side_effect=async_mock)
    return async_mock


@pytest.mark.asyncio
async def test_get_loans(mock_retrieve_loans):
    """
    Get loans test
    """
    mock_retrieve_loans.return_value = loans

    result = await loan_route.get_loans("")

    assert result == loans


@pytest.mark.asyncio
async def test_get_loans_not_found(mock_retrieve_loans):
    """
    Get loans not found test
    """
    mock_retrieve_loans.return_value = []

    result = await loan_route.get_loans("")

    assert result == []


@pytest.mark.asyncio
async def test_get_loans_by_user_id(mock_retrieve_loans_by_user_id):
    """
    Get loans by user id test
    """
    mock_retrieve_loans_by_user_id.return_value = loans

    user_id = uuid4()

    result = await loan_route.get_loans(str(user_id))

    mock_retrieve_loans_by_user_id.assert_called_with(str(user_id))

    assert result == loans


@pytest.mark.asyncio
async def test_get_loans_by_user_id_not_found(mock_retrieve_loans_by_user_id):
    """
    Get loans by user id not found test
    """
    mock_retrieve_loans_by_user_id.return_value = []

    user_id = uuid4()

    result = await loan_route.get_loans(str(user_id))

    mock_retrieve_loans_by_user_id.assert_called_with(str(user_id))

    assert result == []


@pytest.mark.asyncio
async def test_get_loan_by_id(mock_retrieve_loan_by_id):
    """
    Get loan by id test
    """
    mock_retrieve_loan_by_id.return_value = loans[0]

    result = await loan_route.get_loan_by_id(str(loans[0].id))

    mock_retrieve_loan_by_id.assert_called_with(str(loans[0].id))

    assert result == loans[0]


@pytest.mark.asyncio
async def test_get_loan_by_id_not_found(mock_retrieve_loan_by_id):
    """
    Get loan by id not found test
    """
    mock_retrieve_loan_by_id.return_value = None

    try:
        await loan_route.get_loan_by_id(str(loans[0].id))
    except HTTPException as e:
        assert e.status_code == 404
        assert e.detail == "Loan not found"

        mock_retrieve_loan_by_id.assert_called_with(str(loans[0].id))
    else:
        raise pytest.fail("Test failed due to error not being caught")


@pytest.mark.asyncio
async def test_get_loan_schedule(mock_retrieve_loan_schedule):
    """
    Get loan schedule test
    """
    mock_retrieve_loan_schedule.return_value = loans_schedules[0]

    result = await loan_route.get_loan_schedule(str(loans[0].id))

    mock_retrieve_loan_schedule.assert_called_with(str(loans[0].id))

    assert result == loans_schedules[0]


@pytest.mark.asyncio
async def test_get_loan_schedule_not_found(mock_retrieve_loan_schedule):
    """
    Get loan schedule not found test
    """
    mock_retrieve_loan_schedule.return_value = None

    try:
        await loan_route.get_loan_schedule(str(loans[0].id))
    except HTTPException as e:
        assert e.status_code == 404
        assert e.detail == "Loan schedule not found"

        mock_retrieve_loan_schedule.assert_called_with(str(loans[0].id))
    else:
        raise pytest.fail("Test failed due to error not being caught")


@pytest.mark.asyncio
async def test_get_loan_summary(mock_retrieve_loan_summary):
    """
    Get loan summary test
    """
    mock_retrieve_loan_summary.return_value = loans_summaries[0]

    result = await loan_route.get_loan_summary(str(loans[0].id), 5)

    mock_retrieve_loan_summary.assert_called_with(str(loans[0].id), 5)

    assert result == loans_summaries[0]


@pytest.mark.asyncio
async def test_get_loan_summary_not_found(mock_retrieve_loan_summary):
    """
    Get loan summary not found test
    """
    mock_retrieve_loan_summary.return_value = None

    try:
        await loan_route.get_loan_summary(str(loans[0].id), 2)
    except HTTPException as e:
        assert e.status_code == 404
        assert e.detail == "Loan summary not found"

        mock_retrieve_loan_summary.assert_called_with(str(loans[0].id), 2)
    else:
        raise pytest.fail("Test failed due to error not being caught")


@pytest.mark.asyncio
async def test_get_loan_summary_invalid_month(mock_retrieve_loan_summary):
    """
    Get loan summary invalid month test
    """
    mock_retrieve_loan_summary.return_value = None

    try:
        await loan_route.get_loan_summary(str(loans[0].id), 13)
    except HTTPException as e:
        assert e.status_code == 400
        assert e.detail == "Invalid month"

        mock_retrieve_loan_summary.assert_not_called()
    else:
        raise pytest.fail("Test failed due to error not being caught")


@pytest.mark.asyncio
async def test_create_loan(mock_create_loan):
    """
    Create loan test
    """
    mock_create_loan.return_value = loans[1]

    user_id = uuid4()

    result = await loan_route.create_loan(
        CreateLoanRequest(
            user_id,
            loans[1].amount,
            loans[1].annual_interest_rate,
            loans[1].loan_term,
        )
    )

    mock_create_loan.assert_called_once()

    mock_create_loan.assert_called_once_with(
        Attrs(
            amount=loans[1].amount,
            annual_interest_rate=loans[1].annual_interest_rate,
            loan_term=loans[1].loan_term,
        ),
        user_id,
    )

    assert result == loans[1]


@pytest.mark.asyncio
async def test_create_loan_missing_user_id(mock_create_loan):
    """
    Create loan missing user_id test
    """
    mock_create_loan.return_value = loans[1]

    try:
        await loan_route.create_loan(
            CreateLoanRequest(
                None,
                loans[1].amount,
                loans[1].annual_interest_rate,
                loans[1].loan_term,
            )
        )
    except ValidationError as e:
        errors = e.errors()
        assert len(errors) == 1
        assert errors[0]["msg"] == "UUID input should be a string, bytes or UUID object"

        mock_create_loan.assert_not_called()
    else:
        raise pytest.fail("Test failed due to error not being caught")


@pytest.mark.asyncio
async def test_create_loan_invalid_amount(mock_create_loan):
    """
    Create loan missing name test
    """
    mock_create_loan.return_value = loans[1]

    user_id = uuid4()

    try:
        await loan_route.create_loan(
            CreateLoanRequest(
                user_id,
                0,
                loans[1].annual_interest_rate,
                loans[1].loan_term,
            ),
        )
    except ValidationError as e:
        errors = e.errors()
        assert len(errors) == 1
        assert errors[0]["msg"] == "Input should be greater than 0"

        mock_create_loan.assert_not_called()
    else:
        raise pytest.fail("Test failed due to error not being caught")
