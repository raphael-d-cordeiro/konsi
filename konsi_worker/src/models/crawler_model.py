import datetime
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base


DBBaseModel = declarative_base()


class CrawlerModel(DBBaseModel):
    __tablename__ = 'crawlers'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    task_id: str = Column(String(), unique=True, index=True, nullable=False)
    document: str = Column(String(20), index=True, nullable=False)
    crawler_data: str = Column(
        JSONB(),
        index=True,
        nullable=True
    )
    created_at: Date = Column(
        Date,
        default=datetime.datetime.utcnow,
        index=True
    )
