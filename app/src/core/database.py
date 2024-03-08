from typing import List
from peewee import *
import os
from dotenv import load_dotenv

load_dotenv()


class ConfigDatabase:
    db = MySQLDatabase(
        os.getenv('DATABASE_NAME'),
        user=os.getenv('DATABASE_USER'),
        password=os.getenv('DATABASE_PASSWORD'),
        host=os.getenv('DATABASE_HOST'),
        port = int(os.getenv('DATABASE_PORT'))
    )

    def __init__(self, models: List[str]):
        self.models = models

    def refresh_tables(self):
        self.db.create_tables(self.models)


class BaseModel(Model):
    class Meta:
        database = ConfigDatabase.db
