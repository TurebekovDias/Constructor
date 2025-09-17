import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "Dias")
DB_PASSWORD = os.getenv("DB_PASSWORD", "ConstructorPass") 
DB_NAME = os.getenv("DB_NAME", "ConstructorDB")

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

class Base(DeclarativeBase):
    pass

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def create_tables():
    from src.models.user import User
    Base.metadata.create_all(bind=engine)