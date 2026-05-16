from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.sale_schema import (
    SaleCreate,
    SaleResponse
)

from services.sale_service import (
    create_sale_service,
    get_sales_history_service,
    get_sale_by_id_service
)

from auth.auth_bearer import get_current_user


router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)


@router.post(
    "/",
    response_model=SaleResponse
)
def create_sale(

    sale: SaleCreate,

    current_user = Depends(get_current_user),

    db: Session = Depends(get_db)
):

    return create_sale_service(
        db,
        sale,
        current_user
    )


@router.get(
    "/",
    response_model=list[SaleResponse]
)
def get_sales_history(

    current_user = Depends(get_current_user),

    db: Session = Depends(get_db)
):

    return get_sales_history_service(
        db,
        current_user
    )

@router.get(
    "/{sale_id}",
    response_model=SaleResponse
)
def get_sale_by_id(

    sale_id: int,

    current_user = Depends(get_current_user),

    db: Session = Depends(get_db)
):

    return get_sale_by_id_service(
        db,
        sale_id,
        current_user
    )