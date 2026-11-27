from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.conversation import (
    ConversationCreate,
    ConversationResponse,
    ConversationDetailResponse
)
from app.schemas.message import MessageCreate, ChatSendResponse
from app.services.chat_service import ChatService

router = APIRouter(prefix="/conversations", tags=["Conversations"])


@router.post(
    "",
    response_model=ConversationDetailResponse,
    status_code=status.HTTP_201_CREATED
)
def create_conversation(
    data: ConversationCreate,
    db: Session = Depends(get_db)
):
    service = ChatService(db)

    try:
        conversation_id = service.create_conversation(data.first_message)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    return service.get_conversation(conversation_id)


@router.get("", response_model=list[ConversationResponse])
def list_conversations(db: Session = Depends(get_db)):
    service = ChatService(db)
    return service.list_conversations()


@router.get("/{conversation_id}", response_model=ConversationDetailResponse)
def get_conversation(
    conversation_id: int,
    db: Session = Depends(get_db)
):
    service = ChatService(db)
    conversation = service.get_conversation(conversation_id)

    if conversation is None:
        raise HTTPException(status_code=404, detail="Conversa não encontrada.")

    return conversation



@router.post(
    "/{conversation_id}/messages",
    response_model=ChatSendResponse,
    status_code=status.HTTP_200_OK
)
def create_message(
    conversation_id: int,
    data: MessageCreate,
    db: Session = Depends(get_db)
):
    service = ChatService(db)

    try:
        messages = service.send_message(
            conversation_id=conversation_id,
            content=data.content
        )

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    except RuntimeError as error:
        raise HTTPException(status_code=502, detail=str(error))

    if messages is None:
        raise HTTPException(
            status_code=404,
            detail="Conversa não encontrada."
        )

    return messages
