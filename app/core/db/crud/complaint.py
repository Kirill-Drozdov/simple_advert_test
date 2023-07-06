from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.db.crud.base import CRUDBase
from app.core.db.models import Complaint


class CRUDComplaint(CRUDBase):
    async def get_complaints_for_advert(
        self,
        advert_id: int,
        session: AsyncSession,
    ) -> list[Complaint]:
        """Получить все жалобы на объявление."""
        complaints = await session.execute(
            select(self.model).where(
                self.model.advert_id == advert_id
            )
        )
        return complaints.scalars().all()


complaint_crud = CRUDComplaint(Complaint)
