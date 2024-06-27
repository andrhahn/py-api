"""
Database service
"""

from sqlmodel import Session, SQLModel, create_engine


_engine = create_engine("sqlite://", echo=True)

SQLModel.metadata.create_all(_engine)

print("Successfully connected to database")


def get_session() -> Session:
    """
    Get database session
    """

    print("Creating database session")

    return Session(_engine)
