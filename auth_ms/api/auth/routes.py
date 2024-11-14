from fastapi import APIRouter, Request

# from ...dependencies.auth import login
from . import controller

router = APIRouter()
router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/authenticate")
def authenticate_user(request: Request):
    return controller.authenticate_user(request.state.user)
