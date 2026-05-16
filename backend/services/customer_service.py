from fastapi import HTTPException

from sqlalchemy.orm import Session

from models.customer import Customer


def create_customer_service(
    db: Session,
    customer
):

    existing_customer = db.query(Customer).filter(
        Customer.phone == customer.phone
    ).first()

    if existing_customer:

        raise HTTPException(
            status_code=400,
            detail="Phone number already exists"
        )

    new_customer = Customer(
        name=customer.name,
        phone=customer.phone
    )

    db.add(new_customer)

    db.commit()

    db.refresh(new_customer)

    return new_customer


def get_customer_by_phone_service(
    db: Session,
    phone: str
):

    customer = db.query(Customer).filter(
        Customer.phone == phone
    ).first()

    if not customer:

        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer