"""
Loan route
"""

from fastapi import HTTPException
from src.model.loan import Loan
from src.service import loan_service

from src.model.loan import CreateLoanRequest


async def get_loans(user_id: str) -> [Loan]:
    """
    Get all loans
    """

    return await loan_service.retrieve_loans(user_id)


async def get_loan_by_id(id_: str) -> Loan | None:
    """
    Get loan by id
    """

    result = await loan_service.retrieve_loan_by_id(id_)

    if not result:
        raise HTTPException(status_code=404, detail="Loan not found")

    return result


async def get_loan_schedule(id_: str) -> Loan | None:
    """
    Get loan schedule
    """

    result = await loan_service.retrieve_loan_schedule(id_)

    if not result:
        raise HTTPException(status_code=404, detail="Loan schedule not found")

    return result


async def get_loan_summary(id_: str) -> Loan | None:
    """
    Get loan summary
    """

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
        create_loan_request.shared_user_ids,
        create_loan_request.amount,
        create_loan_request.annual_interest_rate,
        create_loan_request.loan_term,
    )

    return await loan_service.create_loan(loan)
