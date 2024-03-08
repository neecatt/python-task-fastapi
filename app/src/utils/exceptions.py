from fastapi import HTTPException, status

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

user_already_registered_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Username already registered",
)

incorrect_login_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect username or password",
    headers={"WWW-Authenticate": "Bearer"},
)

refresh_token_expired_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Refresh token expired or invalid",
    headers={"WWW-Authenticate": "Bearer"},
)

invalid_ip_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Invalid IP address",
)
