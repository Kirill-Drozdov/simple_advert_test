from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.advert import Advert


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
