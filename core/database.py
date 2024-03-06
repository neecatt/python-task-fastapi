from peewee import MySQLDatabase, Model, CharField, DateTimeField, ForeignKeyField
import os
from dotenv import load_dotenv

load_dotenv()


db = MySQLDatabase(
    os.getenv('DATABASE_NAME'),
    user=os.getenv('DATABASE_USER'),
    password=os.getenv('DATABASE_PASSWORD'),
    host=os.getenv('DATABASE_HOST'),
    port=int(os.getenv('DATABASE_PORT'))
)


class User(Model):
    username = CharField(unique=True)
    password = CharField()
    created_at = DateTimeField()

    class Meta:
        database = db


class Task(Model):
    user = ForeignKeyField(User, backref='tasks')
    task_description = CharField()
    created_at = DateTimeField()

    class Meta:
        database = db


db.connect()
db.create_tables([User, Task])
