from sqlalchemy import (
    Column,
    Integer,
    Float,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database import Base

from sqlalchemy.orm import relationship


class SaleItem(Base):

    __tablename__ = "sale_items"

    id = Column(Integer, primary_key=True, index=True)

    sale_id = Column(
        Integer,
        ForeignKey("sales.id")
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    quantity = Column(Integer, nullable=False)

    price = Column(Float, nullable=False)

    subtotal = Column(Float, nullable=False)

    sale = relationship(
        "Sale",
        back_populates="items"
    )

    product = relationship("Product")