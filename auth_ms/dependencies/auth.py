from fastapi import Depends, FastAPI, HTTPException, Request, Security
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBase
from google.auth.transport import requests
from google.oauth2 import id_token

from ..settings import Settings


def init_app(app: FastAPI) -> None:
    app.router.dependencies.append(Depends(validate_google_token))


def validate_google_token(
    request: Request,
    authorization: HTTPAuthorizationCredentials | None = Security(
        HTTPBase(scheme="bearer", auto_error=False)
    ),
):
    """
    Validate google token
    """
    if not authorization:
        d = {
            "loc": ["header", "Authorization"],
            "msg": "Missing Authorization header.",
            "type": "MissingHeader",
        }

        raise HTTPException(401, detail=d)

    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(
            authorization.credentials,
            requests.Request(),
            Settings().GOOGLE_CLIENT_ID,
        )

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        userid = idinfo["sub"]
        useremail = idinfo["email"]

    except Exception as e:
        if isinstance(e, ValueError):
            raise HTTPException(status_code=401, detail="Invalid token")
        else:
            raise HTTPException(status_code=401, detail="Unable to validate token")

    request.state.user = {"id": userid, "email": useremail}
