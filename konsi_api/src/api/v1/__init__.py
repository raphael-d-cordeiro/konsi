from fastapi import APIRouter
from konsi_api.src.api.v1.endpoints import bots

api_router = APIRouter()
api_router.include_router(
    bots.router, prefix='/bots', tags=['bots']
)
