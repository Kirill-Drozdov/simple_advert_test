from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.db.crud.base import CRUDBase
from app.core.db.models import Feedback


class CRUDFeedback(CRUDBase):
    async def get_feedbacks_for_advert(
        self,
        advert_id: int,
        session: AsyncSession,
    ) -> list[Feedback]:
        """Получить все отзывы на объявление."""
        feedbacks = await session.execute(
            select(self.model).where(
                self.model.advert_id == advert_id
            )
        )
        return feedbacks.scalars().all()


feedback_crud = CRUDFeedback(Feedback)
