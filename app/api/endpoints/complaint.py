from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user, current_superuser
from app.crud.advert import advert_crud
from app.crud.complaint import complaint_crud
from app.models import User
from app.schemas.complaint import (
    ComplaintCreate,
    ComplaintDB,
    ComplaintUpdate,
)
from app.validators import (
    check_user_update_delete_rights,
    check_user_create_rights,
)

complaint_router = APIRouter()


@complaint_router.post(
    '/',
    response_model=ComplaintDB,
    status_code=HTTPStatus.CREATED,
    summary="Оставить жалобу",
    response_description="Информация об оставленной жалобе",
)
async def create_new_complaint(
        complaint: ComplaintCreate,
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session),
):
    """Оставить жалобу.

    - **text**: текст жалобы
    - **advert_id**: id внешний ключ объявления
    """
    advert = await advert_crud.get(
        complaint.advert_id,
        session,
    )
    await check_user_create_rights(advert, user)
    return await complaint_crud.create(complaint, user, session)


@complaint_router.get(
    '/',
    response_model=list[ComplaintDB],
    status_code=HTTPStatus.OK,
    summary="Смотреть все жалобы",
    response_description="Список всех жалоб",
    dependencies=[Depends(current_superuser)],
)
async def get_all_complaints(
        session: AsyncSession = Depends(get_async_session),
):
    """Смотреть все жалобы.

    - **text**: текст жалобы
    - **advert_id**: id внешний ключ объявления
    - **id**: уникальный идентификатор жалобы
    - **user_id**: внешний ключ пользователя, оставившего жалобу
    """
    return await complaint_crud.get_multi(session)


@complaint_router.get(
    '/{complaint_id}',
    response_model=ComplaintDB,
    status_code=HTTPStatus.OK,
    summary="Смотреть жалобу по id",
    response_description="Данные жалобы",
    dependencies=[Depends(current_superuser)],

)
async def get_complaint(
        complaint_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """Смотреть одну жалобу.

    - **text**: текст жалобы
    - **advert_id**: id внешний ключ объявления
    - **id**: уникальный идентификатор жалобы
    - **user_id**: внешний ключ пользователя, оставившего жалобу
    """
    return await complaint_crud.get(
        complaint_id, session
    )


@complaint_router.patch(
    '/{complaint_id}',
    response_model=ComplaintDB,
    response_model_exclude_none=True,
    status_code=HTTPStatus.OK,
    summary="Обновить жалобу по id",
    response_description="Данные обновленной жалобы",
)
async def partially_update_complaint(
        complaint_id: int,
        obj_in: ComplaintUpdate,
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session),
):
    """Обновить жалобу.

    - **text**: текст жалобы
    - **advert_id**: id внешний ключ объявления
    """
    complaint = await complaint_crud.get(
        complaint_id, session
    )
    await check_user_update_delete_rights(complaint, user)

    return await complaint_crud.update(
        complaint, obj_in, session
    )


@complaint_router.delete(
    '/{complaint_id}',
    response_model=ComplaintDB,
    response_model_exclude_none=True,
    status_code=HTTPStatus.OK,
    summary="Удалить жалобу по id",
    response_description="Данные удаленной жалобы",
)
async def remove_complaint(
        complaint_id: int,
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session),
):
    """Удалить жалобу.

    - **text**: текст жалобы
    - **advert_id**: id внешний ключ объявления
    - **id**: уникальный идентификатор жалобы
    - **user_id**: внешний ключ пользователя, оставившего жалобу
    """
    complaint = await complaint_crud.get(
        complaint_id, session
    )
    await check_user_update_delete_rights(complaint, user)
    return await complaint_crud.remove(
        complaint, session
    )
