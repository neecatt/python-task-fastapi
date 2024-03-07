from pydantic import BaseModel


class CurrentUserResponse(BaseModel):
    id: int
    username: str
    created_at: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "user",
                "created_at": "2022-01-01T00:00:00",
            }
        }
