from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Uvicorn config
    HOST: str = "0.0.0.0"
    RELOAD: bool = False
    GOOGLE_CLIENT_ID: str = "YOUR_GOOGLE_CLIENT_ID"
    JWT_PRIVATE_KEY: str = "example_key"
    JWT_PLUBLIC_KEY: str = "example_key"
    WORKERS: int = 2
    USERS_MS_URL: str = "http://localhost:8000/v1"
    MONGO_DB_URL: str = "mongodb://localhost:27017"
    MONGO_DB_NAME: str = "users-ms"
    PORT: int = 8000
    API_SECRET: str = "super-secret"

    class Config:
        env_file = ".env"
