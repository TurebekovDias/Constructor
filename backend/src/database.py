import os
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import sessionmaker

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "Dias")
DB_PASSWORD = os.getenv("DB_PASSWORD", "ConstructorPass") 
DB_NAME = os.getenv("DB_NAME", "ConstructorDB")

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}, echo=True"

Base = DeclarativeBase()

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)