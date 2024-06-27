"""
Main
"""

from fastapi import FastAPI, Path
from src.router import user_route
from src.router import loan_route
from src.model.user import CreateUserRequest
from src.model.loan import CreateLoanRequest


app = FastAPI()


@app.get("/users")
async def get_users():
    """
    Get all users
    """
    return await user_route.get_users()


@app.get("/users/{id_}")
async def get_user_by_id(id_: str = Path()):
    """
    Get user by id
    """
    return await user_route.get_user_by_id(id_)


@app.post("/users")
async def create_user(create_user_request: CreateUserRequest):
    """
    Create user
    """
    return await user_route.create_user(create_user_request)


@app.get("/loans")
async def get_loans(user_id: str = None):
    """
    Get all loans, optional user_id query param
    """
    return await loan_route.get_loans(user_id)


@app.get("/loans/{id_}")
async def get_loan_by_id(id_: str = Path()):
    """
    Get loan by id
    """
    return await loan_route.get_loan_by_id(id_)


@app.get("/loans/{id_}/schedule")
async def get_loan_schedule(id_: str = Path()):
    """
    Get loan schedule
    """
    return await loan_route.get_loan_schedule(id_)


@app.get("/loans/{id_}/summary")
async def get_loan_summary(id_: str = Path()):
    """
    Get loan summary
    """
    return await loan_route.get_loan_summary(id_)


@app.post("/loans")
async def create_loan(create_loan_request: CreateLoanRequest):
    """
    Create loan
    """
    return await loan_route.create_loan(create_loan_request)
