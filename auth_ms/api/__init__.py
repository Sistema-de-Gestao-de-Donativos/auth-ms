from fastapi import APIRouter, FastAPI

from . import auth


def init_app(app: FastAPI) -> None:
    router = get_router()
    app.include_router(router)


def get_router() -> APIRouter:
    api_router = APIRouter(prefix="/v1")
    api_router.include_router(auth.auth_router)
    return api_router
