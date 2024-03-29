import datetime
from peewee import CharField, TextField
from ..core.database import BaseModel


class ModelUser(BaseModel):
    username = CharField(unique=True, null=False, max_length=20)
    password_hash = CharField(null=False)
    refresh_token = TextField(null=True)
    created_at = CharField(
        default=datetime.datetime.now().isoformat(), null=False)

    class Meta:
        table_name = "users"
