from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db.db import get_async_session
from app.core.user import current_user
from app.core.db.crud.advert import advert_crud
from app.core.db.crud.feedback import feedback_crud
from app.core.db.models import User
from app.api.schemas.feedback import (
    FeedbackCreate,
    FeedbackDB,
    FeedbackUpdate,
)
from app.core.validators import (
    check_user_update_delete_rights,
    check_user_create_rights,
)

feedback_router = APIRouter()


@feedback_router.post(
    '/',
    response_model=FeedbackDB,
    status_code=HTTPStatus.CREATED,
    summary="Оставить отзыв",
    response_description="Информация об оставленном отзыве",
)
async def create_new_feedback(
        feedback: FeedbackCreate,
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session),
):
    """Оставить отзыв.

    - **text**: текст отзыва
    - **advert_id**: id внешний ключ объявления
    """
    advert = await advert_crud.get(
        feedback.advert_id,
        session,
    )
    await check_user_create_rights(advert, user)
    return await feedback_crud.create(feedback, user, session)


@feedback_router.get(
    '/',
    response_model=list[FeedbackDB],
    status_code=HTTPStatus.OK,
    summary="Смотреть все отзывы",
    response_description="Список всех отзывов",
)
async def get_all_feedbacks(
        session: AsyncSession = Depends(get_async_session),
):
    """Смотреть все отзывы.

    - **text**: текст отзыва
    - **advert_id**: id внешний ключ объявления
    - **id**: уникальный идентификатор отзыва
    - **user_id**: внешний ключ пользователя, оставившего отзыв
    """
    return await feedback_crud.get_multi(session)


@feedback_router.get(
    '/{feedback_id}',
    response_model=FeedbackDB,
    status_code=HTTPStatus.OK,
    summary="Смотреть отзыв по id",
    response_description="Данные отзыва",

)
async def get_advert(
        feedback_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """Смотреть один отзыв.

    - **text**: текст отзыва
    - **advert_id**: id внешний ключ объявления
    - **id**: уникальный идентификатор отзыва
    - **user_id**: внешний ключ пользователя, оставившего отзыв
    """
    return await feedback_crud.get(
        feedback_id, session
    )


@feedback_router.patch(
    '/{feedback_id}',
    response_model=FeedbackDB,
    response_model_exclude_none=True,
    status_code=HTTPStatus.OK,
    summary="Обновить отзыв по id",
    response_description="Данные обновленного отзыва",
)
async def partially_update_advert(
        feedback_id: int,
        obj_in: FeedbackUpdate,
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session),
):
    """Обновить отзыв.

    - **text**: текст отзыва
    - **advert_id**: id внешний ключ объявления
    """
    feedback = await feedback_crud.get(
        feedback_id, session
    )
    await check_user_update_delete_rights(feedback, user)

    return await feedback_crud.update(
        feedback, obj_in, session
    )


@feedback_router.delete(
    '/{feedback_id}',
    response_model=FeedbackDB,
    response_model_exclude_none=True,
    status_code=HTTPStatus.OK,
    summary="Удалить отзыв по id",
    response_description="Данные удаленного отзыва",
)
async def remove_advert(
        feedback_id: int,
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session),
):
    """Удалить отзыв.

    - **text**: текст отзыва
    - **advert_id**: id внешний ключ объявления
    - **id**: уникальный идентификатор отзыва
    - **user_id**: внешний ключ пользователя, оставившего отзыв
    """
    feedback = await feedback_crud.get(
        feedback_id, session
    )
    await check_user_update_delete_rights(feedback, user)
    return await feedback_crud.remove(
        feedback, session
    )
