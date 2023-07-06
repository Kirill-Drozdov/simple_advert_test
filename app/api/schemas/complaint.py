from typing import Optional

from pydantic import BaseModel, Extra, Field, validator


class ComplaintBase(BaseModel):
    """Базовая схема для жалобы."""
    text: Optional[str]

    @validator('text')
    def text_cannot_be_null(cls, value: str):
        if value is None:
            raise ValueError(
                'Текст жалобы не может быть пустым!'
            )
        return value

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1


class ComplaintCreate(ComplaintBase):
    """Схема для создания жалобы."""
    text: str = Field(...,)
    advert_id: int


class ComplaintUpdate(ComplaintBase):
    """Схема для обновления жалобы."""
    pass


class ComplaintDB(ComplaintBase):
    """Схема для получения жалобы."""
    id: int
    user_id: Optional[int]
    advert_id: Optional[int]

    class Config:
        orm_mode = True
