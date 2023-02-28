from typing import Literal, Optional, List, Dict, Any

from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

import os


class Postgres:

    def __init__(self, user: str, pwd: str, server_name: str,
                 database: str, port: str = '5432'):

        self._db_url: URL = URL.create(
            drivername='postgresql+psycopg2',
            username=os.getenv('USER'),
            password=os.getenv('PWD'),
            host=os.getenv('HOST'),
            database=os.getenv('DATABASE'),
            port=port,
        )

    def get_engine(self):
        return create_engine(
            self._db_url,
            client_encoding='utf8',
            connect_args={'connect_timeout': 20}
        )

    def get_session(self):
        engine = self.get_engine()

        return sessionmaker(
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
            bind=engine
        )

    def execute_query(self, query_string: str, query_type: Literal['r', 'w'],
                      **kwargs):
        Engine = self.get_engine()

        _query_stmt = text(query_string)

        with Engine.connect() as connection:
            if query_type == 'r':
                result = connection.execute(_query_stmt, **kwargs)

                if not result:
                    return

                result_data = [dict(row._mapping) for row in result]

                return result_data

            connection.execute(_query_stmt, **kwargs)

        return

    def read_sql_file(self,
                      sql_path: str,
                      name: str):
        if name[-4:] != ".sql":
            name += ".sql"
        file_ = os.path.join(sql_path, name)
        with open(file_, 'rU') as f:
            return f.read()

    def execute_from_file(self,
                          sql_path: str,
                          name: str,
                          query_type: Literal['r', 'w'],
                          **kwargs) -> Optional[List[Dict[str, Any]]]:

        query_stmt = self.read_sql_file(sql_path, name)

        return self.execute_query(query_stmt, query_type, **kwargs)
