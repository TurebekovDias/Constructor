from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class MessageRequest(BaseModel):
    content: str
    chat_id: Optional[int] = None

class MessageResponse(BaseModel):
    id: int
    content: str
    chat_id: int
    timestamp: datetime
    email: str

class ChatHistory(BaseModel):
    messages: List[MessageResponse]
    total: int