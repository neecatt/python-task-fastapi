from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..utils.constants import SECRET_KEY, ALGORITHM
from ..users.schemas import SchemaUser
from .services import add_user_db,  login_for_access_token


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
