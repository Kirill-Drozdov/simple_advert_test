from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.advert import (
    create_advert,
    check_advert_description_is_unique,
    get_all_adverts_from_db,
)
from app.schemas.advert import (
    AdvertCreate,
    AdvertDB,
)

router = APIRouter(
    prefix='/adverts',
    tags=['Advert'],
)


@router.post(
    '/',
    response_model=AdvertDB,
)
async def create_new_advert(
        advert: AdvertCreate,
        session: AsyncSession = Depends(get_async_session),
):
    """Разместить объявление."""
    await check_advert_description_is_unique(advert.description, session)
    return await create_advert(advert, session)


@router.get(
    '/',
    response_model=list[AdvertDB],
)
async def get_all_adverts(
        session: AsyncSession = Depends(get_async_session),
):
    """Смотреть все объявления."""
    return await get_all_adverts_from_db(session)
