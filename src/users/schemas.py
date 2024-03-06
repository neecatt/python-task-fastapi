from pydantic import BaseModel
from typing import Optional
import datetime


class SchemaUser(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "user",
                "password": "password",
            }
        }
