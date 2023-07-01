import enum

from sqlalchemy import Column, Enum, String, Text, Integer

from app.core.db import Base


class Advert(Base):
    """Модель объявления."""
    class Kind(str, enum.Enum):
        """Вид объявления."""

        BUYING = "Покупка"
        SELLING = "Продажа"
        SERVICE = "Услуга"

    title = Column(String(100), nullable=False)
    description = Column(Text, unique=True, nullable=False)
    kind = Column(
        Enum(
            Kind,
            name="kind_of_service",
        ),
        nullable=False,
    )
    price = Column(Integer, nullable=False)
