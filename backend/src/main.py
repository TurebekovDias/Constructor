from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api import main_router
from src.database import create_tables

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    print("Creating database tables...")
    create_tables()
    print("Database tables created successfully!")

app.include_router(main_router)

@app.get("/")
async def root():
    return {"message": "FastAPI Auth API is running!"}