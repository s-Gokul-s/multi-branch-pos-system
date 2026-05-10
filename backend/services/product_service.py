from sqlalchemy.orm import Session
from models.products import Product
from fastapi import HTTPException

def create_product_service(db : Session, product ):

    new_product = Product(
        name = product.name,
        category = product.category,
        price = product.price,
        barcode = product.barcode    
    )

    existing_product = db.query(Product).filter(
        Product.barcode == product.barcode
    ).first()

    if existing_product:
        raise HTTPException(
            status_code=400,
            detail="barcode already exist"
        )

    db.add(new_product)

    db.commit()

    db.refresh(new_product)

    return new_product


def get_product_service(db : Session):
    products = db.query(Product).all()

    return products



def update_product_service(db:Session, product_id, product):
    existing_product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not existing_product:
        raise HTTPException(
            status_code= 400,
            detail="Product not found")
    
    existing_product.name = product.name
    existing_product.category = product.category
    existing_product.price = product.price
    existing_product.barcode = product.barcode

    db.add(existing_product)

    db.commit()

    db.refresh(existing_product)

    return existing_product
        


def delete_product_service(db : Session,product_id : int):
    existing_product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not existing_product:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    
    db.delete(existing_product)

    db.commit()

    return {
        "message": "Product deleted successfully"
    }

