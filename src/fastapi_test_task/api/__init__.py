from fastapi import APIRouter

from .user_api import router as users_router
from .book_api import router as books_router


router = APIRouter()

router.include_router(users_router)
router.include_router(books_router)