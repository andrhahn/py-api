"""
Main
"""

from fastapi import FastAPI
from src.router import user_route
from src.router import loan_route

app = FastAPI()

app.include_router(user_route.router)
app.include_router(loan_route.router)
