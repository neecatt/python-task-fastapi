from audioop import add
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from httpx import get
from jose import jwt, JWTError
from .responses import CurrentUserResponse
from ..utils.constants import SECRET_KEY, ALGORITHM
from ..users.models import ModelUser
from ..users.schemas import SchemaUser
from ..users.responses import UserResponse
from .utils import get_password_hash, verify_password
from ..utils.exceptions import credentials_exception, user_already_registered_exception, incorrect_login_exception
from .services import add_user_db, get_user_by_token, login_for_access_token


router_auth = APIRouter(
    prefix="/api/v1/auth",
    tags=["auth"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Register a user
@router_auth.post("/signup", summary="Create a user", status_code=status.HTTP_201_CREATED)
async def create_user(request: SchemaUser):
    return await add_user_db(request.username, request.password)


# Login a user
@router_auth.post("", summary="Login a user", status_code=status.HTTP_200_OK)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return await login_for_access_token(form_data)


# Get current user
@router_auth.get("/me", summary="Get current user", status_code=status.HTTP_200_OK)
async def get_current_user(token: str):
    user_data = get_user_by_token(token).__data__
    return CurrentUserResponse(**user_data)
