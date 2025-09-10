from fastapi import APIRouter

from src.api.auth.auth import router as auth_router
from src.api.AI.chat import router as chat_router

main_router = APIRouter()

main_router.include_router(auth_router)
main_router.include_router(chat_router)