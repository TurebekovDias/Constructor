import os
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "Dias")
DB_PASSWORD = os.getenv("DB_PASSWORD", "ConstructorPass") 
DB_NAME = os.getenv("DB_NAME", "ConstructorDB")

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    username = Column(String,index=True)
    email = Column(String, primary_key=True, unique=True, index=True)
    password = Column(String)

def create_tables():
    Base.metadata.create_all(bind=engine)