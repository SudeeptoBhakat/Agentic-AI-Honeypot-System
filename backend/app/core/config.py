from pydantic_settings import BaseSettings
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    APP_NAME: str
    DEBUG: bool

    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int

    MODEL_PATH: str

    class Config:
        env_file = BASE_DIR / ".env"
        extra = "forbid"

    @property
    def DATABASE_URL(self) -> str:
        password = quote_plus(self.DB_PASS)
        return (
            f"postgresql://{self.DB_USER}:{password}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()
