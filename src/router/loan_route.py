"""
Loan route
"""

from fastapi import HTTPException
from src.model.loan import Loan, LoanSchedule, LoanSummary
from src.service import loan_service
from src.util import uuid_util

from src.model.loan import CreateLoanRequest


async def get_loans(user_id: str | None) -> [Loan]:
    """
    Get all loans
    """

    if user_id and not uuid_util.is_valid_uuid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user id")

    return await loan_service.retrieve_loans(user_id)


async def get_loan_by_id(id_: str) -> Loan | None:
    """
    Get loan by id
    """

    if not uuid_util.is_valid_uuid(id_):
        raise HTTPException(status_code=400, detail="Invalid loan id")

    result = await loan_service.retrieve_loan_by_id(id_)

    if not result:
        raise HTTPException(status_code=404, detail="Loan not found")

    return result


async def get_loan_schedule(id_: str) -> LoanSchedule | None:
    """
    Get loan schedule
    """

    if not uuid_util.is_valid_uuid(id_):
        raise HTTPException(status_code=400, detail="Invalid loan id")

    result = await loan_service.retrieve_loan_schedule(id_)

    if not result:
        raise HTTPException(status_code=404, detail="Loan schedule not found")

    return result


async def get_loan_summary(id_: str) -> LoanSummary | None:
    """
    Get loan summary
    """

    if not uuid_util.is_valid_uuid(id_):
        raise HTTPException(status_code=400, detail="Invalid loan id")

    result = await loan_service.retrieve_loan_summary(id_)

    if not result:
        raise HTTPException(status_code=404, detail="Loan summary not found")

    return result


async def create_loan(create_loan_request: CreateLoanRequest) -> Loan | None:
    """
    Create loan
    """

    loan = Loan(
        None,
        create_loan_request.user_id,
        create_loan_request.amount,
        create_loan_request.annual_interest_rate,
        create_loan_request.loan_term,
    )

    return await loan_service.create_loan(loan)
