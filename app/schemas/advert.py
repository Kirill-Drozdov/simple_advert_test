from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt, validator

from app.models.advert import Advert


class AdvertBase(BaseModel):
    """Базовая схема для объявления."""
    title: Optional[str] = Field(None, max_length=100)
    description: Optional[str]
    kind: Optional[Advert.Kind]
    price: Optional[PositiveInt]

    @validator('title')
    def title_cannot_be_null(cls, value: str):
        if value is None:
            raise ValueError(
                'Название не может быть пустым!'
            )
        return value

    @validator('description')
    def description_cannot_be_null(cls, value: str):
        if value is None:
            raise ValueError(
                'Описание не может быть пустым!'
            )
        return value

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1


class AdvertCreate(AdvertBase):
    """Схема для создания объявления."""
    title: str = Field(..., max_length=100)
    description: str = Field(...,)
    kind: Advert.Kind = Field(...,)
    price: PositiveInt = Field(...,)


class AdvertUpdate(AdvertBase):
    """Схема для обновления объявления."""
    pass


class AdvertDB(AdvertBase):
    """Схема для получения объявления."""
    id: int
    user_id: Optional[int]

    class Config:
        orm_mode = True
