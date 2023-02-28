import asyncio
import uvicorn
from fastapi import FastAPI
from create_table import create_tables

from core.configs import settings
from api.v1 import api_router

app = FastAPI(
    title='KONSI API',
    version='1.0.0',
    description='REST API'
)

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    asyncio.run(create_tables())
    uvicorn.run(
        'main:app', host='0.0.0.0',
        port=8000, reload=True, log_level='info'
    )
