import os
from datetime import datetime,timedelta

from jose import jwt, JWTError
from dotenv import load_dotenv
from fastapi import HTTPException

from passlib.context import CryptContext

from core.config import settings



SECRET_KEY = settings.SECRET_KEY

ALGORITHM = settings.ALGORITHM


pwd_context = CryptContext(
    schemes = ["bcrypt"],
    deprecated = "auto"
)

def hash_password(password : str):

    return pwd_context.hash(password)

def verify_password(plain_password : str,
                    hashed_password : str):
    
    return pwd_context.verify(plain_password,hashed_password)


def create_acess_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=30)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt



def verify_acess_token(token:str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload
    
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail = "Invalid or expired token"
        )