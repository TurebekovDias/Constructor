from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt
# from openai import OpenAI

import auth, models, utils



app = FastAPI()

@app.get("/")
async def checkhealth():
    return {"Check": "Well"}

@app.get("/auth")
async def get_auth_status():
    pass

@app.post("/chat")
async def chat_with_ai():
    pass
