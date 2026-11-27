from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict


class MessageCreate(BaseModel):
    content: str


class MessageResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    role: Literal["user", "assistant", "system"]
    content: str
    created_at: datetime

class ChatSendResponse(BaseModel):
    user_message: MessageResponse
    assistant_message: MessageResponse
