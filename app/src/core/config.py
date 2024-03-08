from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.users.models import ModelUser


ALL_MODELS = [ModelUser]


def middlewareAPI(app: FastAPI, available=True):
    if available:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
