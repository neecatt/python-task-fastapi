from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..utils.constants import SECRET_KEY, ALGORITHM
from ..users.schemas import SchemaUser
from .services import add_user_db, get_user_by_token,  login_for_access_token, refresh_access_token


router_auth = APIRouter(
    prefix="/api/v1/auth",
    tags=["auth"]
)

user_dependency = Depends(get_user_by_token)


# Register a user
@router_auth.post("/signup", summary="Create a user", status_code=status.HTTP_201_CREATED)
async def create_user(request: SchemaUser):
    return await add_user_db(request.username, request.password)


# Login a user
@router_auth.post("", summary="Login a user", status_code=status.HTTP_200_OK)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return await login_for_access_token(form_data)


# Refresh access token
@router_auth.post("/refresh", summary="Refresh access token", status_code=status.HTTP_200_OK)
async def refresh_token(current_user: Annotated[SchemaUser, user_dependency]):
    return await refresh_access_token(current_user.refresh_token)
