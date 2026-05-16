from sqlalchemy import (
    Column,
    Integer,
    Float,
    ForeignKey,
    DateTime
)

from sqlalchemy.sql import func

from sqlalchemy.orm import relationship

from database import Base


class Sale(Base):

    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)

    branch_id = Column(
        Integer,
        ForeignKey("branches.id")
    )

    cashier_id = Column(
        Integer,
        ForeignKey("user.id")
    )

    total_amount = Column(Float, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    items = relationship(
        "SaleItem",
        back_populates="sale"
    )

    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=True
    )