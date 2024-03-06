from operator import is_
from src.core.config import ALL_MODELS, middlewareAPI
from src.core.database import ConfigDatabase
import uvicorn as uvicorn
from fastapi import FastAPI
from src.users.routers import router_user
from src.auth.routers import router_auth

app = FastAPI(title="Python task with Celery RabbitMQ FastAPI",
              version="0.1.0")


# Routers
app.include_router(router_user)
app.include_router(router_auth)

# Middleware
middlewareAPI(app)

# Create All Tables

config = ConfigDatabase(ALL_MODELS)


@app.on_event("startup")
async def startup():
    if config.db.is_closed():
        config.db.connect()
        print("Connected to the database")
        config.refresh_tables()
        print("Refreshing tables")


@app.on_event("shutdown")
async def shutdown():
    print("Shutting down")
    if not config.db.is_closed():
        config.db.close()
        print("Disconnected from the database")

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
