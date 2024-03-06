from fastapi import APIRouter, status
from .responses import UserResponse
from .models import ModelUser


router_user = APIRouter(
    prefix="/api/v1/users",
    tags=["user"]
)


# Get all users
@router_user.get("/", summary="Get all users", status_code=status.HTTP_200_OK)
async def get_users():
    return [UserResponse(**i.__data__) for i in ModelUser.select()]


# Get a user by id
@router_user.get("/{id}", summary="Get a user by id", status_code=status.HTTP_200_OK)
async def get_user(id: int):
    return UserResponse(**ModelUser.get_by_id(id).__data__)
