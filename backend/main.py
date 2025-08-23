from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.params import Query
from datetime import datetime, timedelta
from jose import JWTError, jwt
# from openai import OpenAI
from models import SignUpSchema, SignInSchema, TokenRequest
from auth import signup, signin, decode
import utils



app = FastAPI()

@app.get("/")
async def checkhealth():
    return {"Check": "Well"}

@app.get("/auth")
async def get_auth_status():
    pass

@app.post("/signup")
async def sign_up(request: SignUpSchema):
    token = signup(request.username, request.email, request.password)
    return token

@app.post("/signin")
async def sign_in(request: SignInSchema):
    token = signin(request.email, request.password)
    return token

@app.post("/auth")
def auth(token: str = Query(...)):
    decoded_token = decode(token)
    return decoded_token

@app.post("/chat")
async def chat_with_ai():
    pass