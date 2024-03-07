import datetime
from typing import Optional
from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    username: str
    created_at: Optional[datetime.datetime]

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "username": "user",
                "created_at": "2022-01-01T00:00:00"
            }
        }
