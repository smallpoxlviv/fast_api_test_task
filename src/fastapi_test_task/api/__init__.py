from fastapi import APIRouter

from .user_api import router as users_router


router = APIRouter()
router.include_router(users_router)