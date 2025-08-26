from fastapi import APIRouter
from database import engine
from sqlalchemy.orm import sessionmaker

router = APIRouter()

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