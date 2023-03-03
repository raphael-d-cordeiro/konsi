import os

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """
    General Application Config
    """
    DATABASE_USER: str =
    DATABASE_PWD: str = postgres
    DATABASE_HOST: str = postgres
    DATABASE_NAME: str = konsi
    API_V1_STR: str = '/api/v1'
    DB_URL: URL = URL.create(
            drivername='postgresql+asyncpg',
            username=os.environ.get('DATABASE_USER'),
            password=os.environ.get(,
            host=os.environ.get(,
            database=os.environ.get(,
            port=os.environ.get(,
        )"://postgres:123@127.0.0.1:5432/konsi"
    DBBaseModel=declarative_base()

    class Config:
        case_sensitive=True


settings: Settings=Settings()
