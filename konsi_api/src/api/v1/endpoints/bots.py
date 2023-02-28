from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Response
from fastapi import status

from fastapi import Path
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from konsi_api.src.models.bot_model import BotModel
from konsi_api.src.schemas.bot_schema import (
    BotSchema
)
from core.deps import get_session


router = APIRouter()


@router.get('/',
            description='Get all bots data',
            summary='Get all bots',
            response_model=List[BotSchema],
            response_description='Bots Data has found!')
async def get_customers(db: AsyncSession = Depends(get_session)):

    query = select(BotModel)
    result = await db.execute(query)
    customers: List[BotModel] = result.scalars().all()
    return customers


@router.get('/{bot_name}',
            response_model=BotSchema,
            status_code=status.HTTP_200_OK)
async def get_customer(bot_name: int = Path(default=None,
                                            title='ID bot'),
                       db: AsyncSession = Depends(get_session)):
    query = select(BotModel).filter(BotModel.id == bot_name)
    result = await db.execute(query)
    customer = result.scalar_one_or_none()

    if customer:
        return customer
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='customer not found!'
        )


@router.post('/',
             status_code=status.HTTP_201_CREATED,
             response_model=BotSchemaResp)
async def post_customer(customer: BotSchema,
                        db: AsyncSession = Depends(get_session)):
    new_customer = BotModel(
        cpf=customer.cpf,
        nome=customer.nome,
        email=customer.email,
        data_nascimento=customer.data_nascimento,
        sexo=customer.sexo,
        renda_mensal=customer.renda_mensal
    )
    try:
        db.add(new_customer)
        await db.commit()
        return new_customer
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='customer already exists!'
        )
