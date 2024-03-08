from datetime import timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from src.utils.exceptions import credentials_exception, refresh_token_expired_exception
from src.utils.constants import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_DAYS
from src.users.models import ModelUser


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_access_token_expires():
    return datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)


def get_refresh_token_expires():
    return datetime.now() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = get_access_token_expires()
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict):
    refresh_token_expires = get_refresh_token_expires()
    data.update({"exp": refresh_token_expires})
    refresh_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return refresh_token


def verify_access_token(token: str):
    try:
        if token is None:
            raise refresh_token_expired_exception
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = ModelUser.get_or_none(username=username)
    if user is None:
        raise credentials_exception
    return user


def verify_refresh_token(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return False
    except JWTError:
        return False
    user = ModelUser.get_or_none(username=username)
    if user is None:
        return False
    return True
