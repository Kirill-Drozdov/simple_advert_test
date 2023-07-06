import enum

from sqlalchemy import Column, Enum, ForeignKey, String, Text, Integer
from sqlalchemy.orm import relationship

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
    feedbacks = relationship('Feedback', cascade='delete')

    def __repr__(self):
        return (
            f'Объявление №{self.id} - {self.title}'
        )


class Feedback(Base):
    """Модель отзыва."""
    text = Column(Text, nullable=False)
    advert_id = Column(Integer, ForeignKey(
        'advert.id',
        name='fk_advert_feedback_id_feedback',
    ))
    user_id = Column(Integer, ForeignKey(
        'user.id',
        name='fk_advert_user_id_user',
    ))

    def __repr__(self):
        return (
            f'Отзыв: {self.text[:50]}'
        )


class Complaint(Base):
    """Модель жалобы."""
    text = Column(Text, nullable=False)
    advert_id = Column(Integer, ForeignKey(
        'advert.id',
        name='fk_advert_feedback_id_feedback',
    ))
    user_id = Column(Integer, ForeignKey(
        'user.id',
        name='fk_advert_user_id_user',
    ))

    def __repr__(self):
        return (
            f'Жалоба: {self.text[:50]}'
        )
