from sqlalchemy import Column, String, Text, Integer

from app.core.db import Base


class Advert(Base):
    """Модель объявления."""
    title = Column(String(100), nullable=False)
    description = Column(Text, unique=True, nullable=False)
    price = Column(Integer, nullable=False)
