import time
import jwt
from fastapi import HTTPException
from models import SignUpSchema, SignInSchema

# from passlib.context import CryptContext

import secrets
JWT_SECRET = secrets.token_hex(16)
JWT_ALGORITHM = "HS256"

print(JWT_SECRET)

def sign(email = str):
    payload = {
        "email": email,
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token

def decode(token):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["email"] else None
    
    except:
        raise HTTPException(status_code=401, detail="Invalid token.")

userlist = []

def signup(username = str, email = str, password = str):
    for user in userlist:
        if user['email'] == email:
            raise HTTPException(status_code=400, detail="Email already registered.")
    user = SignUpSchema(username=username, email=email, password=password)
    userlist.append(user)

    token = sign(user.email)    
    return token

def signin(email = str, password = str):
    for user in userlist:
        if user.email == email and user.password == password:
            token = sign(user.email)
            return token
    raise HTTPException(status_code=401, detail="Invalid email or password.")