import enum

from sqlalchemy import Column, Enum, ForeignKey, String, Text, Integer

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
    user_id = Column(Integer, ForeignKey(
        'user.id',
        name='fk_advert_user_id_user',
    ))

    def __repr__(self):
        return (
            f'Объявление №{self.id} - {self.title}'
        )
