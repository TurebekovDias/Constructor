from fastapi import APIRouter
from src.database import engine
from sqlalchemy.orm import sessionmaker
from fastapi.security import OAuth2PasswordRequestForm
from src.api.utils import get_password_hash, verify_password, create_access_token
from src.schemas.auth import Token as auth_schema 
from typing import Annotated
from fastapi import Depends, HTTPException, status

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

Session = sessionmaker(engine)

# routers would be added here
@router.get("/")
async def health_check():
    return {"status": "ok"}

@router.post("/signin")
async def signin():
    return {"message": "Sign-in endpoint"}

@router.post("/signup")
async def signup():
    return {"message": "Sign-up endpoint"}

def get_user(username: str):
    session = Session()
    user = session.execute(
        "SELECT * FROM users WHERE username = :username", 
        {"username": username}
    ).fetchone()
    return user

def authenticate_user(username: str, password: str):
    session = Session()
    user = session.execute(
        "SELECT * FROM users WHERE username = :username", 
        {"username": username}
    ).fetchone()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

@router.post("/token", response_model=auth_schema)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    session = Session()
    user = session.execute(
        "SELECT * FROM users WHERE username = :username", 
        {"username": form_data.username}
    ).fetchone()
    
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}