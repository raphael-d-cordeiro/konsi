from fastapi import APIRouter
from .endpoints import crawlers

api_router = APIRouter()
api_router.include_router(
    crawlers.router, prefix='/crawlers', tags=['crawlers']
)
