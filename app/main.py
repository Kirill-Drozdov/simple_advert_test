from fastapi import FastAPI

from app.core.config import settings
from app.api.routers import main_router

app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
)

app.include_router(main_router)
