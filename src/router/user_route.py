"""
User route
"""

from fastapi import HTTPException, APIRouter
from src.model.user import User
from src.service import user_service
from src.model.user import CreateUserRequest
from src.util import uuid_util

router = APIRouter()


@router.get("/users")
async def get_users() -> list[User]:
    """
    Get all users
    """

    return await user_service.retrieve_users()


@router.get("/users/{id_}")
async def get_user_by_id(id_: str) -> User | None:
    """
    Get user by id
    """

    if not uuid_util.is_valid_uuid(id_):
        raise HTTPException(status_code=400, detail="Invalid user id")

    result = await user_service.retrieve_user_by_id(id_)

    if not result:
        raise HTTPException(status_code=404, detail="User not found")

    return result


@router.post("/users")
async def create_user(create_user_request: CreateUserRequest) -> User | None:
    """
    Create user
    """

    user = User(None, create_user_request.name, create_user_request.signup_date)

    return await user_service.create_user(user)
