from sqlalchemy import String
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from src.database import Base

class User(Base):
    __tablename__ = "users"

    chats = relationship("Chat", back_populates="user")

    username: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    email: Mapped[str] = mapped_column(String, primary_key=True, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)