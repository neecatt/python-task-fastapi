from typing import Optional
from pydantic import BaseModel


class CurrentUserResponse(BaseModel):
    id: int
    username: str
    created_at: str
    refresh_token: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "username": "user",
                "created_at": "2022-01-01T00:00:00",
                "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxIn0.6Dw7fYv2gXtZ2H2Ft2Z3J4"
            }
        }
