from sqlalchemy.orm import Session

from database.connection import engine
from database.models import Conversation, Message


with Session(engine) as session:

    # Criando uma conversa
    conversation = Conversation(
        title="Estudos de Python"
    )

    # Criando as mensagens
    message1 = Message(
        role="user",
        content="Olá, Jason!"
    )

    message2 = Message(
        role="assistant",
        content="Olá! Como posso ajudá-lo?"
    )

    message3 = Message(
        role="user",
        content="Quero aprender SQLAlchemy."
    )

    # Associando as mensagens à conversa
    conversation.messages.append(message1)
    conversation.messages.append(message2)
    conversation.messages.append(message3)

    # Adicionando a conversa à sessão
    session.add(conversation)

    # Salvando tudo no banco
    session.commit()

    print("Conversa e mensagens salvas!")
    print(f"ID da conversa: {conversation.id}")