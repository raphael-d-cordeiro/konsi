from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import status

from fastapi import Query
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.publisher import celery_app
from models import CrawlerModel
from schemas import (
    CrawlerSchemaPost, CrawlerSchemaResp
)
from core.deps import get_session


router = APIRouter()


@router.get('/',
            response_model=CrawlerSchemaResp,
            status_code=status.HTTP_200_OK)
async def get_crawlers_result(
    task_id: str = Query(
        title='Task id to get results'
    ),
    crawler_filter_result: str = Query(
        default=None,
        title='Filter results by BENEFITS',
        example='BENEFITS_NUMBERS_ONLY'
    ),
        db: AsyncSession = Depends(get_session)):

    query = select(CrawlerModel).filter(CrawlerModel.task_id == task_id)
    result = await db.execute(query)
    results: List[CrawlerModel] = result.scalars().all()

    if results:
        return results
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='customer not found!'
        )


@router.post('/', status_code=status.HTTP_201_CREATED)
async def post_customer(request_body: CrawlerSchemaPost):
    try:
        celery_task = celery_app.send_task(
            'konsi_worker.src.tasks.run_crawlers', args=[request_body.dict()]
        )
        payload = {
            'message': 'placed a task to run in background',
            'task_id': celery_task.id
        }

        return JSONResponse(payload)

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Error creating execution task!'
        )
