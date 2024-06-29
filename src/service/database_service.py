"""
Database service
"""

import logging
import os
from dotenv import load_dotenv
from sqlmodel import Session, SQLModel, create_engine
from src.model import user, loan, user_loan  # pylint: disable=unused-import

load_dotenv()

ENGINE = None


def init() -> None:
    """
    Initialize database
    """

    global ENGINE  # pylint: disable=global-statement

    ENGINE = create_engine(os.getenv("DB_URI"), echo=True)
    ENGINE = create_engine(os.getenv("DB_URI"), echo=True)

    SQLModel.metadata.create_all(ENGINE)

    logging.info("Successfully connected to database")


def get_session() -> Session:
    """
    Get database session
    """

    logging.info("Creating database session")

    return Session(ENGINE)
