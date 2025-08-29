from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str
    
class SignInSchema(BaseModel):
    username: str
    password: str

class SignUpSchema(SignInSchema):
    email: str