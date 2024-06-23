"""
Loan service
"""

from uuid import uuid4
from src.model.loan import Loan, LoanSchedule, LoanSummary
from src.service import user_service


loans = [
    Loan(uuid4(), user_service.users[0].id, [], 1000.00, 19.99, 36),
    Loan(uuid4(), user_service.users[0].id, [], 750.00, 17.75, 30),
    Loan(uuid4(), user_service.users[1].id, [], 500.00, 15.5, 24),
    Loan(uuid4(), user_service.users[2].id, [], 20.00, 1.99, 6),
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


async def retrieve_loans(user_id: str) -> [Loan]:
    """
    Retrieve all loans, optional user_id param
    """

    if user_id:
        result = []
        for loan in loans:
            if str(loan.user_id) == user_id:
                result.append(loan)
        return result
    else:
        return loans


async def retrieve_loan_by_id(id_: str) -> Loan | None:
    """
    Retrieve loan by id
    """
    loan: Loan | None = None

    if id_ == str(loans[0].id):
        loan = loans[0]
    elif id_ == str(loans[1].id):
        loan = loans[1]
    elif id_ == str(loans[2].id):
        loan = loans[2]

    return loan


async def retrieve_loan_schedule(id_: str) -> LoanSchedule | None:
    """
    Retrieve loan schedule
    """
    loan_schedule: LoanSchedule | None = None

    if id_ == str(loans[0].id):
        loan_schedule = loans_schedules[0]
    elif id_ == str(loans[1].id):
        loan_schedule = loans_schedules[1]
    elif id_ == str(loans[2].id):
        loan_schedule = loans_schedules[2]

    return loan_schedule


async def retrieve_loan_summary(id_: str) -> LoanSummary | None:
    """
    Retrieve loan summary
    """
    loan_summary: LoanSummary | None = None

    if id_ == str(loans[0].id):
        loan_summary = loans_summaries[0]
    elif id_ == str(loans[1].id):
        loan_summary = loans_summaries[1]
    elif id_ == str(loans[2].id):
        loan_summary = loans_summaries[2]

    return loan_summary


async def create_loan(loan: Loan) -> Loan | None:
    """
    Create loan
    """
    loan.id = uuid4()

    loans.append(loan)

    return loan
