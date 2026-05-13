from pydantic import BaseModel,EmailStr
from enum import Enum


class UserRole(str, Enum):

    admin = "admin"

    manager = "manager"

    cashier = "cashier"

class UserCreate(BaseModel):
    
    name : str

    email : EmailStr

    password : str

    role : UserRole

    branch_id: int | None = None


class UserResponse(BaseModel):

    id : int

    name : str

    email : EmailStr

    role : UserRole

    branch_id: int | None

    class Config:
        from_attributes = True


class UserLogin(BaseModel):

    email: EmailStr

    password: str