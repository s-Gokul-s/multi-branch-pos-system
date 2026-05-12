from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.user_schema import (
    UserCreate,
    UserResponse,
    UserLogin
)

from services.auth_service import (
    register_user_service,
    login_user_service
)



router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    return register_user_service(
        db,
        user
    )


@router.post("/login")
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    return login_user_service(
        db,
        user
    )