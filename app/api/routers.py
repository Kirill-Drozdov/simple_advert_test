from fastapi import APIRouter

from app.api.endpoints.advert import advert_router
from app.api.endpoints.feedback import feedback_router
from app.api.endpoints.user import user_router

main_router = APIRouter()

main_router.include_router(
    advert_router,
    prefix='/adverts',
    tags=['Advert'],
)
main_router.include_router(
    feedback_router,
    prefix='/feedbacks',
    tags=['Feedback'],
)
main_router.include_router(user_router)
