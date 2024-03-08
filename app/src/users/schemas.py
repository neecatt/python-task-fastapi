from pydantic import BaseModel
from typing import Optional


class SchemaUser(BaseModel):
    username: str
    password: str
    created_at: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "username": "user",
                "password": "password",
                "created_at": "2022-01-01T00:00:00"
            }
        }
