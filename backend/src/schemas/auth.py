from pydantic import BaseModel

class SignInSchema(BaseModel):
    username: str
    password: str

class SignUpSchema(SignInSchema):
    email: str