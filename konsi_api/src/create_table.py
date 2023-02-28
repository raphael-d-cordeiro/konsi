import asyncio
from core.configs import settings
from core.database import engine
import models  # noqa


async def create_tables() -> None:
    async with engine.begin() as conn:
        print('Creating Tables if not exists...')
        # create tables sqlalchemy models
        await conn.run_sync(
            settings.DBBaseModel.metadata.create_all
        )
        print('Done!...')


if __name__ == '__main__':
    asyncio.run(create_tables())
