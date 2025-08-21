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
@app.get("/test")
async def test():
    return auth.test()