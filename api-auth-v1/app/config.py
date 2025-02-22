from typing import Any, Dict, Optional

from pydantic import BaseSettings, EmailStr, SecretStr, validator


class Settings(BaseSettings):
    PROJECT_NAME: str = "API Auth"  

    POSTGRES_DB: str = "api_auth"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: SecretStr = SecretStr("postgres")
    POSTGRES_URI: Optional[str] = None

    @validator("POSTGRES_URI", pre=True)
    def validate_postgres_conn(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(v, str):
            return v
        password: SecretStr = values.get("POSTGRES_PASSWORD", SecretStr(""))
        return "{scheme}://{user}:{password}@{host}/{db}".format(
            scheme="postgresql+asyncpg",
            user=values.get("POSTGRES_USER"),
            password=password.get_secret_value(),
            host=values.get("POSTGRES_HOST"),
            db=values.get("POSTGRES_DB"),
        )

    FIRST_USER_EMAIL: EmailStr = "admin@example.com"
    FIRST_USER_PASSWORD: SecretStr = SecretStr("admin")

    SECRET_KEY: SecretStr = SecretStr("secret")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7


settings = Settings()