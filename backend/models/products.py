from sqlalchemy import Column, Integer, String, Float
from database import Base
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=True)

    category = Column(String)

    price = Column(Float,nullable=False)
    
    barcode = Column(String,unique = True)

    inventories = relationship(
        "Inventory",
        back_populates="product")