
from sqlalchemy.orm import Session

from app.repositories.chat_repository import ChatRepository
from app.services.agent_service import AgentService


class ChatService:

    def __init__(self, db: Session):
        self.repository = ChatRepository(db)
        self.agent = AgentService()

    def create_conversation(self, first_message: str):

        if not first_message.strip():
            raise ValueError("A mensagem inicial não pode estar vazia.")

        return self.repository.create_conversation(first_message)

    def save_message(
        self,
        conversation_id: int,
        content: str,
        role: str = "user"
    ):

        if not content.strip():
            raise ValueError("A mensagem não pode estar vazia.")

        conversation = self.repository.get_conversation(conversation_id)

        if conversation is None:
            return None

        return self.repository.save_message(
            conversation_id=conversation_id,
            role=role,
            content=content
        )

    def get_conversation(self, conversation_id: int):
        return self.repository.get_conversation(conversation_id)

    def list_conversations(self):
        return self.repository.list_conversations()

    
    def send_message(self, conversation_id: int, content: str):

        # 1. Verifica se a conversa existe
        conversation = self.repository.get_conversation(conversation_id)

        if conversation is None:
            return None

        if not content.strip():
            raise ValueError("A mensagem não pode estar vazia.")

        # 2. Salva a mensagem do usuário
        self.repository.save_message(
            conversation_id=conversation_id,
            role="user",
            content=content
        )

        # 3. Recupera o histórico atualizado
        conversation = self.repository.get_conversation(conversation_id)

        # 4. Organiza o histórico para o Agent
        messages = [
            {
                "role": message.role,
                "content": message.content
            }
            for message in sorted(
                conversation.messages,
                key=lambda message: message.id
            )
        ]

        # 5. Envia o histórico ao Agent
        assistant_content = self.agent.send_message(messages)

        # 6. Salva a resposta do Agent
        self.repository.save_message(
            conversation_id=conversation_id,
            role="assistant",
            content=assistant_content
        )

        # 7. Recupera as mensagens persistidas
        conversation = self.repository.get_conversation(conversation_id)

        messages = sorted(
            conversation.messages,
            key=lambda message: message.id
        )

        return {
            "user_message": messages[-2],
            "assistant_message": messages[-1]
        }

