from fastapi import APIRouter, Depends, HTTPException
from src.api.auth.utils import get_current_active_user

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)

@router.get("/")
async def chat_health():
    return {"status": "chat service is running"}

@router.post("/message")
async def send_message(
    message: str,
    current_user: str = Depends(get_current_active_user)
):    
    return {
        "user": current_user,
        "message": message,
        "response": f"Ответ ИИ на сообщение: {message}"
    }

@router.get("/history")
async def get_chat_history(
    current_user: str = Depends(get_current_active_user)
):
    # Здесь будет логика получения истории чата
    return {
        "user": current_user,
        "history": ["Пример истории чата"]
    }