from fastapi import APIRouter, Depends, Query

from sqlalchemy.orm import Session

from database import get_db

from schemas.inventory_schema import (
    InventoryCreate,
    InventoryResponse,
    InventoryUpdate,
    InventoryDetailedResponse
)

from services.inventory_service import (
    create_inventory_service,
    get_inventory_service,
    update_inventory_service,
    search_inventory_service
)

from auth.auth_bearer import get_current_user
from auth.role_checker import admin_required


router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


@router.post(
    "/",
    response_model=InventoryResponse
)
def create_inventory(

    inventory: InventoryCreate,

    current_user = Depends(get_current_user),

    db: Session = Depends(get_db)
):

    admin_required(current_user)

    return create_inventory_service(
        db,
        inventory
    )


@router.get(
    "/",
    response_model=list[InventoryDetailedResponse]
)
def get_inventory(

    current_user = Depends(get_current_user),

    db: Session = Depends(get_db)
):

    return get_inventory_service(
        db,
        current_user)

@router.get(
    "/search",
    response_model=list[InventoryDetailedResponse]
)
def search_inventory(

    product: str = Query(...),

    current_user = Depends(get_current_user),

    db: Session = Depends(get_db)):

    return search_inventory_service(
        db,
        product,
        current_user
    )


@router.put(
    "/{inventory_id}",
    response_model=InventoryResponse
)
def update_inventory(

    inventory_id: int,

    inventory: InventoryUpdate,

    current_user = Depends(get_current_user),

    db: Session = Depends(get_db)
):

    admin_required(current_user)

    return update_inventory_service(
        db,
        inventory_id,
        inventory
    )