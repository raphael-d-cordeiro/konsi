import os

from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv


load_dotenv()


class DBConnection:

    def __init__(self):

        self._db_url: URL = URL.create(
            drivername='postgresql+psycopg2',
            username=os.environ.get('DATABASE_USER'),
            password=os.environ.get('DATABASE_PWD'),
            host=os.environ.get('DATABASE_HOST'),
            database=os.environ.get('DATABASE_NAME'),
            port=os.environ.get('DATABASE_PORT')
        )

    def get_engine(self):
        return create_engine(
            self._db_url,
            client_encoding='utf8',
            connect_args={'connect_timeout': 20}
        )

    def __enter__(self):
        engine = self.get_engine()
        session_maker = sessionmaker(
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
            bind=engine
        )
        self.session = session_maker(bind=engine)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
