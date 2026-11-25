from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Conversation(Base):

    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(150), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )

    messages: Mapped[list["Message"]] = relationship(
        back_populates="conversation",
        cascade="all, delete-orphan"
    )


class Message(Base):

    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    conversation_id: Mapped[int] = mapped_column(
        ForeignKey("conversations.id"),
        nullable=False
    )

    role: Mapped[str] = mapped_column(String(20), nullable=False)

    content: Mapped[str] = mapped_column(Text, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )

    conversation: Mapped["Conversation"] = relationship(
        back_populates="messages"
    )
