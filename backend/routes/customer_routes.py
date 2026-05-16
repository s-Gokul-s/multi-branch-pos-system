from fastapi import (
    APIRouter,
    Depends,
    Query
)

from sqlalchemy.orm import Session

from database import get_db

from schemas.customer_schema import (
    CustomerCreate,
    CustomerResponse
)

from services.customer_service import (
    create_customer_service,
    get_customer_by_phone_service
)

from auth.auth_bearer import get_current_user


router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post(
    "/",
    response_model=CustomerResponse
)
def create_customer(

    customer: CustomerCreate,

    current_user = Depends(get_current_user),

    db: Session = Depends(get_db)
):

    return create_customer_service(
        db,
        customer
    )


@router.get(
    "/search",
    response_model=CustomerResponse
)
def search_customer(

    phone: str = Query(...),

    current_user = Depends(get_current_user),

    db: Session = Depends(get_db)
):

    return get_customer_by_phone_service(
        db,
        phone
    )