from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    General Application Config
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:123@127.0.0.1:5432/konsi_api"
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings: Settings = Settings()
