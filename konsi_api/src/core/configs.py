import os

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """
    General Application Config
    """

    DB_URL: str = (
        'postgresql+asyncpg://{user}:{pwd}@{host}:{port}/{db}'.format(
            user=os.environ.get('DATABASE_USER'),
            pwd=os.environ.get('DATABASE_PWD'),
            host=os.environ.get('DATABASE_HOST'),
            port=os.environ.get('DATABASE_PORT'),
            db=os.environ.get('DATABASE_NAME')
        )
    )
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings: Settings = Settings()
