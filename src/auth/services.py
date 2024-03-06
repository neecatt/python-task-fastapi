from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .utils import create_access_token, create_refresh_token, get_access_token_expires, get_password_hash, get_refresh_token_expires, verify_password, verify_token
from ..users.models import ModelUser
from ..users.responses import UserResponse
from ..utils.exceptions import user_already_registered_exception, credentials_exception, incorrect_login_exception

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def add_user_db(username: str, password: str):
    user = ModelUser(username=username, password=password)
    if user.get_or_none(username=username):
        raise user_already_registered_exception
    user.password_hash = get_password_hash(password)
    user.save()
    return UserResponse(**user.__data__)


def authenticate_user(username: str, password: str):
    user = ModelUser.get_or_none(username=username)
    if user is None or not verify_password(password, user.password_hash):
        raise credentials_exception
    return user


def get_user_by_token(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    return user


async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise incorrect_login_exception
    access_token_expires = get_access_token_expires()
    refresh_token_expires = get_refresh_token_expires()
    access_token = create_access_token(
        data={"sub": user.username})
    refresh_token = create_refresh_token(
        data={"sub": user.username})
    user.refresh_token = refresh_token
    user.save()
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}
