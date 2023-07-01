from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.advert import (
    create_advert,
    check_advert_description_is_unique,
    delete_advert,
    get_all_adverts_from_db,
    get_advert_by_id,
    update_advert,
)
from app.schemas.advert import (
    AdvertCreate,
    AdvertDB,
    AdvertUpdate,
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


@router.get(
    '/{advert_id}',
    response_model=AdvertDB,
)
async def get_advert(
        advert_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """Смотреть одно объявление."""
    return await get_advert_by_id(
        advert_id, session
    )


@router.patch(
    '/{advert_id}',
    response_model=AdvertDB,
    response_model_exclude_none=True,
)
async def partially_update_advert(
        advert_id: int,
        obj_in: AdvertUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    """Обновить объявление."""
    advert = await get_advert_by_id(
        advert_id, session
    )
    if obj_in.description is not None:
        await check_advert_description_is_unique(obj_in.description, session)

    return await update_advert(
        advert, obj_in, session
    )


@router.delete(
    '/{advert_id}',
    response_model=AdvertDB,
    response_model_exclude_none=True,
)
async def remove_advert(
        advert_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """Удалить объявление."""
    advert = await get_advert_by_id(
        advert_id, session
    )
    return await delete_advert(
        advert, session
    )
