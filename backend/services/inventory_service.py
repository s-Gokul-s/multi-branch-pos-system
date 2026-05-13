from fastapi import HTTPException

from sqlalchemy.orm import Session

from models.inventory import Inventory

from models.products import Product

def create_inventory_service(
    db: Session,
    inventory
):

    existing_inventory = db.query(Inventory).filter(
        Inventory.branch_id == inventory.branch_id,
        Inventory.product_id == inventory.product_id
    ).first()

    if existing_inventory:

        raise HTTPException(
            status_code=400,
            detail="Inventory already exists"
        )

    new_inventory = Inventory(
        branch_id=inventory.branch_id,
        product_id=inventory.product_id,
        stock=inventory.stock
    )

    db.add(new_inventory)

    db.commit()

    db.refresh(new_inventory)

    return new_inventory


def get_inventory_service(
    db: Session,
    current_user
):

    if current_user["role"] == "admin":

        return db.query(Inventory).all()

    return db.query(Inventory).filter(
        Inventory.branch_id == current_user["branch_id"]
        ).all()


def update_inventory_service(
    db: Session,
    inventory_id: int,
    inventory
    ):

        existing_inventory = db.query(Inventory).filter(
            Inventory.id == inventory_id
        ).first()

        if not existing_inventory:

            raise HTTPException(
                status_code=404,
                detail="Inventory not found"
            )

        existing_inventory.stock = inventory.stock

        db.commit()

        db.refresh(existing_inventory)

        return existing_inventory

def search_inventory_service(
    db: Session,
    product_name: str,
    current_user):

    query = db.query(Inventory).join(Product)

    query = query.filter(
        Product.name.ilike(f"%{product_name}%")
    )

    if current_user["role"] != "admin":

        query = query.filter(
            Inventory.branch_id == current_user["branch_id"]
        )

    return query.all()