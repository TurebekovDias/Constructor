from sqlalchemy import String
from sqlalchemy.orm import  Mapped, mapped_column
from database import Base


class UserBase(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String, primary_key=True, unique=True, index=True)
    password: Mapped[str] = mapped_column(String)

# for future use in history tracking
# class HistoryBase(DeclarativeBase):
#     __tablename__ = "history"

#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     name: Mapped[str] = mapped_column(String(50))
#     email: Mapped[str] = mapped_column(String, index=True, ForeignKey("users.email"))