from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    """Настройки проекта."""
    APP_TITLE: str = 'SimpleAdvert'
    APP_DESCRIPTION: str = 'Сервис для удобного размещения объявлений'
    DATABASE_URL: str
    SECRET: str = 'letspythonizetheworld:)'
    FIRST_SUPERUSER_EMAIL: EmailStr = 'admin@ya.ru'
    FIRST_SUPERUSER_PASSWORD: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
