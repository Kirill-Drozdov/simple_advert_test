from typing import Optional

from pydantic import BaseModel, Extra, Field, validator


class FeedbackBase(BaseModel):
    """Базовая схема для отзыва."""
    text: Optional[str]

    @validator('text')
    def text_cannot_be_null(cls, value: str):
        if value is None:
            raise ValueError(
                'Текст отзыва не может быть пустым!'
            )
        return value

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1


class FeedbackCreate(FeedbackBase):
    """Схема для создания отзыва."""
    text: str = Field(...,)
    advert_id: int


class FeedbackUpdate(FeedbackBase):
    """Схема для обновления отзыва."""
    pass


class FeedbackDB(FeedbackBase):
    """Схема для получения отзыва."""
    id: int
    user_id: Optional[int]
    advert_id: Optional[int]

    class Config:
        orm_mode = True
