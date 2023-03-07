import datetime

from core.configs import settings
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import JSONB


class CrawlerModel(settings.DBBaseModel):
    __tablename__ = 'crawlers'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    task_id: str = Column(String(), unique=True, index=True, nullable=False)
    document: str = Column(String(20), index=True, nullable=False)
    crawler_data: dict = Column(
        JSONB(),
        index=True,
        nullable=True
    )
    created_at: Date = Column(
        Date,
        default=datetime.datetime.utcnow,
        index=True
    )
