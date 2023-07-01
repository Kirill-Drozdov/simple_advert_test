from pydantic import BaseSettings


class Settings(BaseSettings):
    """Настройки проекта."""
    APP_TITLE: str = 'SimpleAdvert'
    APP_DESCRIPTION: str = 'Сервис для удобного размещения объявлений'
    DATABASE_URL: str
    SECRET: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()
