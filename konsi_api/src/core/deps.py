from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from core.database import Session


class TokenData(BaseModel):
    username: Optional[str] = None


async def get_session() -> AsyncSession:
    async with Session() as session:
        yield session
