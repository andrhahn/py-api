"""
User models
"""

from datetime import datetime
from uuid import UUID, uuid4
from pydantic import AwareDatetime, BaseModel, Field


class User(BaseModel):
    """
    User model
    """

    id: UUID | None = Field(default_factory=uuid4)
    name: str = Field(min_length=3)
    signup_date: datetime = AwareDatetime()

    def __init__(self, _id, name, signup_date):
        super().__init__(name=name, signup_date=signup_date)


class CreateUserRequest(BaseModel):
    """
    CreateUserRequest model
    """

    name: str = Field(min_length=3)
    signup_date: datetime = AwareDatetime()

    def __init__(self, name, signup_date):
        super().__init__(name=name, signup_date=signup_date)
