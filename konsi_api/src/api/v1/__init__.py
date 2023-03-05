from fastapi import APIRouter
from konsi_api.src.api.v1.endpoints import crawlers

api_router = APIRouter()
api_router.include_router(
    crawlers.router, prefix='/crawlers', tags=['crawlers']
)
