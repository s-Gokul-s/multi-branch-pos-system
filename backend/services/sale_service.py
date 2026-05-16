from fastapi import HTTPException

from sqlalchemy.orm import Session

from models.sale import Sale
from models.sale_item import SaleItem

from models.products import Product
from models.inventory import Inventory
from models.customer import Customer


def create_sale_service(
    db: Session,
    sale,
    current_user
):

    total_amount = 0

    customer = None

    if sale.customer_id:

        customer = db.query(Customer).filter(
            Customer.id == sale.customer_id
        ).first()

        if not customer:

            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )

    sale_items = []

    for item in sale.items:

        product = db.query(Product).filter(
            Product.id == item.product_id
        ).first()

        if not product:

            raise HTTPException(
                status_code=404,
                detail=f"Product {item.product_id} not found"
            )

        inventory = db.query(Inventory).filter(
            Inventory.product_id == item.product_id,
            Inventory.branch_id == current_user["branch_id"]
        ).first()

        if not inventory:

            raise HTTPException(
                status_code=404,
                detail=f"Inventory not found for product {product.name}"
            )

        if inventory.stock < item.quantity:

            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for {product.name}"
            )

        subtotal = product.price * item.quantity

        total_amount += subtotal

        inventory.stock -= item.quantity

        sale_item = {
            "product_id": product.id,
            "quantity": item.quantity,
            "price": product.price,
            "subtotal": subtotal
        }

        sale_items.append(sale_item)

    new_sale = Sale(
        branch_id=current_user["branch_id"],
        cashier_id=current_user["user_id"],
        customer_id=sale.customer_id,
        total_amount=total_amount
    )

    db.add(new_sale)

    db.commit()

    db.refresh(new_sale)

    for item in sale_items:

        new_item = SaleItem(
            sale_id=new_sale.id,
            product_id=item["product_id"],
            quantity=item["quantity"],
            price=item["price"],
            subtotal=item["subtotal"]
        )

        db.add(new_item)
        
    if customer:

        earned_points = int(total_amount // 100)

        customer.loyalty_points += earned_points

    db.commit()

    db.refresh(new_sale)

    return new_sale


def get_sales_history_service(
    db: Session,
    current_user
):

    query = db.query(Sale)

    if current_user["role"] != "admin":

        query = query.filter(
            Sale.branch_id == current_user["branch_id"]
        )

    return query.all()



def get_sale_by_id_service(
    db: Session,
    sale_id: int,
    current_user
):

    sale = db.query(Sale).filter(
        Sale.id == sale_id
    ).first()

    if not sale:

        raise HTTPException(
            status_code=404,
            detail="Sale not found"
        )

    if current_user["role"] != "admin":

        if sale.branch_id != current_user["branch_id"]:

            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

    return sale