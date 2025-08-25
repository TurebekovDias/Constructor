from fastapi import APIRouter

router = APIRouter()

# routers would be added here
@router.get("/")
async def health_check():
    return {"status": "ok"}