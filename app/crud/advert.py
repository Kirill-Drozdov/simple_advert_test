from typing import Optional

from fastapi import HTTPException
# from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.advert import Advert
from app.schemas.advert import AdvertCreate


async def check_advert_description_is_unique(
        advert_description: str,
        session: AsyncSession,
) -> None:
    """Проверка описания объявления на уникальность."""
    exists_criteria = (
        select(Advert).where(
            Advert.description == advert_description
        ).exists()
    )
    db_advert_exists = await session.execute(
        select(True).where(
            exists_criteria
        )
    )
    db_advert_exists = db_advert_exists.scalars().first()
    if db_advert_exists:
        raise HTTPException(
            status_code=422,
            detail='Придумайте уникальное описание объявления!',
        )


async def get_advert_by_id(
        advert_id: int,
        session: AsyncSession,
) -> Optional[Advert]:
    """
    Возвращает объявление по id.
    Если объявление не найдено, бросает ошибку.
    """
    db_advert = await session.execute(
        select(Advert).where(
            Advert.id == advert_id
        )
    )
    advert = db_advert.scalars().first()
    if advert is None:
        raise HTTPException(
            status_code=404,
            detail='Объявление не найдено!'
        )
    return advert


async def create_advert(
        new_advert: AdvertCreate,
        session: AsyncSession,
) -> Advert:
    """Создать объявление в БД."""
    new_advert_data = new_advert.dict()
    db_advert = Advert(**new_advert_data)

    session.add(db_advert)
    await session.commit()
    await session.refresh(db_advert)

    return db_advert


async def get_all_adverts_from_db(
        session: AsyncSession,
) -> list[Advert]:
    """Возвращает все объявления из БД."""
    db_adverts = await session.execute(select(Advert))
    return db_adverts.scalars().all()
