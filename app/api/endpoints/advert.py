from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.advert import advert_crud
from app.models import User
from app.schemas.advert import (
    AdvertCreate,
    AdvertDB,
    AdvertUpdate,
)
from app.validators import (
    check_advert_description_is_unique,
    check_user_rights,
)

advert_router = APIRouter()


@advert_router.post(
    '/',
    response_model=AdvertDB,
    status_code=HTTPStatus.CREATED,
    summary="Разместить объявление",
    response_description="Информация о созданном объявлении",
)
async def create_new_advert(
        advert: AdvertCreate,
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session),
):
    """Разместить объявление.

    - **title**: название
    - **description**: описание
    - **kind**: вид объявления (Покупка|Продажа|Услуга)
    - **price**: цена
    """
    await check_advert_description_is_unique(
        advert.description,
        session,
    )
    return await advert_crud.create(advert, user, session)


@advert_router.get(
    '/',
    response_model=list[AdvertDB],
    response_model_exclude={'user_id'},
    status_code=HTTPStatus.OK,
    summary="Смотреть все объявления",
    response_description="Список всех объявлений",
)
async def get_all_adverts(
        session: AsyncSession = Depends(get_async_session),
):
    """Смотреть все объявления.

    - **title**: название
    - **description**: описание
    - **kind**: вид объявления (Покупка|Продажа|Услуга)
    - **price**: цена
    - **id**: уникальный идентификатор объявления
    - **user_id**: внешний ключ пользователя, разместившего объявление
    """
    return await advert_crud.get_multi(session)


@advert_router.get(
    '/{advert_id}',
    response_model=AdvertDB,
    status_code=HTTPStatus.OK,
    summary="Смотреть объявление по id",
    response_description="Данные объявления",

)
async def get_advert(
        advert_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """Смотреть одно объявление.

    - **title**: название
    - **description**: описание
    - **kind**: вид объявления (Покупка|Продажа|Услуга)
    - **price**: цена
    - **id**: уникальный идентификатор объявления
    - **user_id**: внешний ключ пользователя, разместившего объявление
    """
    return await advert_crud.get(
        advert_id, session
    )


@advert_router.patch(
    '/{advert_id}',
    response_model=AdvertDB,
    response_model_exclude_none=True,
    status_code=HTTPStatus.OK,
    summary="Обновить объявление по id",
    response_description="Данные обновленного объявления",
)
async def partially_update_advert(
        advert_id: int,
        obj_in: AdvertUpdate,
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session),
):
    """Обновить объявление.

    - **title**: название
    - **description**: описание
    - **kind**: вид объявления (Покупка|Продажа|Услуга)
    - **price**: цена
    """
    advert = await advert_crud.get(
        advert_id, session
    )
    await check_user_rights(advert, user)
    if (obj_in.description is not None
       and obj_in.description != advert.description):
        await check_advert_description_is_unique(
            obj_in.description,
            session,
        )

    return await advert_crud.update(
        advert, obj_in, session
    )


@advert_router.delete(
    '/{advert_id}',
    response_model=AdvertDB,
    response_model_exclude_none=True,
    status_code=HTTPStatus.OK,
    summary="Удалить объявление по id",
    response_description="Данные удаленного объявления",
)
async def remove_advert(
        advert_id: int,
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session),
):
    """Удалить объявление.

    - **title**: название
    - **description**: описание
    - **kind**: вид объявления (Покупка|Продажа|Услуга)
    - **price**: цена
    - **id**: уникальный идентификатор объявления
    - **user_id**: внешний ключ пользователя, разместившего объявление
    """
    advert = await advert_crud.get(
        advert_id, session
    )
    await check_user_rights(advert, user)
    return await advert_crud.remove(
        advert, session
    )
