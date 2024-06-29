"""
Database service
"""

import logging as logger
from sqlmodel import Session, SQLModel, create_engine
from src.model import user, loan, user_loan  # pylint: disable=unused-import


ENGINE = None


def init(db_uri: str = None) -> None:
    """
    Initialize database
    """

    global ENGINE  # pylint: disable=global-statement

    ENGINE = create_engine(db_uri or "sqlite://")

    SQLModel.metadata.create_all(ENGINE)

    logger.info('Successfully connected to database: %s', db_uri)


def get_session() -> Session:
    """
    Get database session
    """

    logger.info("Creating database session")

    return Session(ENGINE)
