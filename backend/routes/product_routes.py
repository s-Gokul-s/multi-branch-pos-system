from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from models.products import Product
from schemas.product_schema import ProductCreate, ProductResponse, ProductUpdate
from services.product_service import (create_product_service, get_product_service,
                                       update_product_service,delete_product_service)

from auth.auth_bearer import get_current_user
from auth.role_checker import admin_required

router = APIRouter(
    prefix = "/api",
    tags= ["Products"]
)


@router.get("/products", response_model=list[ProductResponse])
def get_products(
    current_user = Depends(get_current_user),
    db : Session = Depends(get_db)
): 
    
    return get_product_service(db)



@router.post("/products", response_model=ProductResponse)
def create_products(product : ProductCreate,
                    current_user = Depends(get_current_user),
                    db : Session = Depends(get_db)):
    
    admin_required(current_user)

    return create_product_service(db,product)




@router.put("/products/{product_id}",response_model=ProductUpdate)
def update_product(product_id : int,
                   product : ProductUpdate,
                   current_user = Depends(get_current_user),
                   db : Session = Depends(get_db)):
    
    admin_required(current_user)

    return update_product_service(db, product_id,product)


@router.delete("/products/{product_id}")
def delete_product(product_id : int,
                   current_user = Depends(get_current_user),
                   db : Session = Depends(get_db)):
    
    admin_required(current_user)

    return delete_product_service(db,product_id)
