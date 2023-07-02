from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.advert import advert_crud
from app.schemas.advert import (
    AdvertCreate,
    AdvertDB,
    AdvertUpdate,
)
from app.validators import check_advert_description_is_unique

advert_router = APIRouter()


@advert_router.post(
    '/',
    response_model=AdvertDB,
)
async def create_new_advert(
        advert: AdvertCreate,
        session: AsyncSession = Depends(get_async_session),
):
    """Разместить объявление."""
    await check_advert_description_is_unique(
        advert.description,
        session,
    )
    return await advert_crud.create(advert, session)


@advert_router.get(
    '/',
    response_model=list[AdvertDB],
)
async def get_all_adverts(
        session: AsyncSession = Depends(get_async_session),
):
    """Смотреть все объявления."""
    return await advert_crud.get_multi(session)


@advert_router.get(
    '/{advert_id}',
    response_model=AdvertDB,
)
async def get_advert(
        advert_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """Смотреть одно объявление."""
    return await advert_crud.get(
        advert_id, session
    )


@advert_router.patch(
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
    advert = await advert_crud.get(
        advert_id, session
    )
    if obj_in.description is not None:
        await check_advert_description_is_unique(
            advert.description,
            session,
        )

    return await advert_crud.update(
        advert, obj_in, session
    )


@advert_router.delete(
    '/{advert_id}',
    response_model=AdvertDB,
    response_model_exclude_none=True,
)
async def remove_advert(
        advert_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """Удалить объявление."""
    advert = await advert_crud.get(
        advert_id, session
    )
    return await advert_crud.remove(
        advert, session
    )
