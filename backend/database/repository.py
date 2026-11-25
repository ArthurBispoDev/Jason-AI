
from sqlalchemy.orm import Session

from backend.database.connection import engine
from backend.database.models import Conversation, Message


def create_conversation(first_message: str):

    title = " ".join(first_message.split())

    if len(title) > 50:
        title = title[:47] + "..."

    with Session(engine) as session:

        conversation = Conversation(title=title)

        session.add(conversation)
        session.flush()

        message = Message(
            conversation_id=conversation.id,
            role="user",
            content=first_message
        )

        session.add(message)
        session.commit()

        return conversation.id


def save_message(conversation_id: int, role: str, content: str):

    with Session(engine) as session:

        message = Message(
            conversation_id=conversation_id,
            role=role,
            content=content
        )

        session.add(message)
        session.commit()
