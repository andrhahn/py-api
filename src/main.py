"""
Main
"""

import logging as logger
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from src.router import user_route
from src.router import loan_route
from src.service import database_service

load_dotenv()

logger.getLogger().setLevel(logger.INFO)

database_service.init(os.getenv("DB_URI"))

app = FastAPI()

app.include_router(user_route.router)
app.include_router(loan_route.router)
