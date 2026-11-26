from sqlalchemy.orm import Session

from app.repositories.chat_repository import ChatRepository


class ChatService:

    def __init__(self, db: Session):
        self.repository = ChatRepository(db)

    def create_conversation(self, first_message: str):
        if not first_message.strip():
            raise ValueError("A mensagem inicial não pode estar vazia.")

        return self.repository.create_conversation(first_message)

    def save_message(self, conversation_id: int, content: str, role: str = "user"):
        if not content.strip():
            raise ValueError("A mensagem não pode estar vazia.")

        conversation = self.repository.get_conversation(conversation_id)

        if conversation is None:
            return None

        self.repository.save_message(
            conversation_id=conversation_id,
            role=role,
            content=content
        )

        return self.repository.save_message(
            conversation_id=conversation_id,
            role=role,
            content=content
        )

    def get_conversation(self, conversation_id: int):
        return self.repository.get_conversation(conversation_id)

    def list_conversations(self):
        return self.repository.list_conversations()