from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models import Conversation, Message


class ChatRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_conversation(self, first_message: str):

        title = " ".join(first_message.split())

        if len(title) > 50:
            title = title[:47] + "..."

        conversation = Conversation(title=title)

        self.db.add(conversation)
        self.db.flush()

        message = Message(
            conversation_id=conversation.id,
            role="user",
            content=first_message
        )

        self.db.add(message)
        self.db.commit()

        return conversation.id

    def save_message(self, conversation_id: int, role: str, content: str):
        message = Message(
            conversation_id=conversation_id,
            role=role,
            content=content
        )

        self.db.add(message)
        self.db.commit()

        return message

    
    def get_conversation(self, conversation_id: int):

        statement = (
            select(Conversation)
            .options(selectinload(Conversation.messages))
            .where(Conversation.id == conversation_id)
            .execution_options(populate_existing=True)
        )

        return self.db.scalars(statement).first()


    def list_conversations(self):
        statement = (
            select(Conversation)
            .order_by(Conversation.id.desc())
        )

        return self.db.scalars(statement).all()
