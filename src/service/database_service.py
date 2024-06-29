"""
Database service
"""

from sqlmodel import Session, SQLModel, create_engine
from src.model import user, loan, user_loan # pylint: disable=unused-import

engine = create_engine("sqlite://", echo=True)

SQLModel.metadata.create_all(engine)

print("Successfully connected to database")


def get_session() -> Session:
    """
    Get database session
    """

    print("Creating database session")

    return Session(engine)
