import asyncio
import uvicorn
from fastapi import FastAPI
from core.create_table import create_tables

from api.v1.endpoints import crawlers

app = FastAPI(
    title='KONSI API',
    version='1.0.0',
    description='REST API'
)

app.include_router(
    crawlers.router, prefix='/crawlers', tags=['crawlers']
)

if __name__ == '__main__':
    asyncio.run(create_tables())
    uvicorn.run(
        'main:app', host='0.0.0.0',
        port=8000, reload=True, log_level='info'
    )
