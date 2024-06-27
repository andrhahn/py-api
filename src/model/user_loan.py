"""
UserLoan models
"""

from uuid import UUID, uuid4
from typing import Optional
from sqlmodel import Field, SQLModel


class UserLoan(SQLModel, table=True):
    """
    UserLoan model
    """

    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID
    loan_id: UUID
    is_owner: bool

    def __init__(self, _id, user_id, loan_id, is_owner):
        super().__init__(
            user_id=user_id,
            loan_id=loan_id,
            is_owner=is_owner,
        )
