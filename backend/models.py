from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    hashed_password: str

class User(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"