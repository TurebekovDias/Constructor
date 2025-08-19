from fastapi import FastAPI
from openai import OpenAI

app = FastAPI()

@app.get("/")
async def checkhealth():
    return {"Check": "Well"}