import uvicorn as uvicorn
from fastapi import FastAPI
from core.database import db, User

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run("main:app", port=88000, reload=True)
