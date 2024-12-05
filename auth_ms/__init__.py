from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import api, dependencies


def create_app() -> FastAPI:
    app = FastAPI(title="Auth Microservice", version="0.0.1")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows all origins
        allow_credentials=True,
        allow_methods=["*"],  # Allows all methods
        allow_headers=["*"],  # Allows all headers
    )
    dependencies.init_app(app)
    api.init_app(app)
    return app
