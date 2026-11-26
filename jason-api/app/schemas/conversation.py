from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.message import MessageResponse


class ConversationCreate(BaseModel):
    first_message: str


class ConversationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    created_at: datetime


class ConversationDetailResponse(ConversationResponse):
    messages: list[MessageResponse]