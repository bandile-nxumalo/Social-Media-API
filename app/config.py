from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Support either individual DB pieces or a single DATABASE_URL (Heroku)
    database_hostname: Optional[str]
    database_port: Optional[str]
    database_password: Optional[str]
    database_name: Optional[str]
    database_username: Optional[str]
    database_url: Optional[str]

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"


settings = Settings()