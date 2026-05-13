from sqlalchemy import (
    Column,
    Integer,
    ForeignKey
)

from database import Base

from sqlalchemy.orm import relationship


class Inventory(Base):

    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)

    branch_id = Column(
        Integer,
        ForeignKey("branches.id")
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    stock = Column(Integer, default=0)

    product = relationship(
    "Product",
    back_populates="inventories")

    branch = relationship(
        "Branch",
    back_populates="inventories")