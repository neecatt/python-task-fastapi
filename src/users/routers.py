from typing import Annotated
from fastapi import APIRouter, Depends, status
from ..auth.responses import CurrentUserResponse
from ..auth.services import get_user_by_token
from .schemas import SchemaUser
from .responses import UserResponse
from .models import ModelUser


router_user = APIRouter(
    prefix="/api/v1/users",
    tags=["user"]
)

user_dependency = Depends(get_user_by_token)


# Get all users
@router_user.get("/all", summary="Get all users", status_code=status.HTTP_200_OK)
async def get_users():
    return [UserResponse(**i.__data__) for i in ModelUser.select()]


# Get a user by id
@router_user.get("/{id}", summary="Get a user by id", status_code=status.HTTP_200_OK)
async def get_user(id: int):
    return UserResponse(**ModelUser.get_by_id(id).__data__)


# Get current user
@router_user.get("", summary="Get current user", status_code=status.HTTP_200_OK)
async def get_current_user(current_user: Annotated[SchemaUser, user_dependency]):
    return CurrentUserResponse(username=current_user.username, created_at=current_user.created_at, id=current_user.id)
