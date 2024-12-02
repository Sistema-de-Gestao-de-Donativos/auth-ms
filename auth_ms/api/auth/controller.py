from datetime import datetime, timedelta

import jwt
import requests
from fastapi import HTTPException

from ...settings import Settings

settings = Settings()


def authenticate_user(user: dict):
    """
    Authenticate user by google token and users microservice
    """

    user_email = user.get("email")

    response = requests.get(
        url=f"{settings.USERS_MS_URL}/users/?email={user_email}",
        headers={"Authorization": f"Bearer {settings.API_SECRET}"},
    )

    if response.status_code != 200:
        raise HTTPException(status_code=401, detail="User not found")

    user = response.json()[0]

    # Define the JWT payload
    payload = {
        "sub": user["_id"],
        "email": user["email"],
        "role": user["role"],
        "exp": datetime.now() + timedelta(days=1),  # Token expires in 1 day
    }

    # Generate the JWT token
    token = jwt.encode(payload, settings.JWT_PRIVATE_KEY, algorithm="RS256")

    return {"access_token": token, "token_type": "bearer"}
