from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    
class SignInSchema(BaseModel):
    username: str
    password: str

class SignUpSchema(SignInSchema):
    email: str