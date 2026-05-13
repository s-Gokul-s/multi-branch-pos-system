from sqlalchemy import Column, Integer, String

from database import Base
from sqlalchemy.orm import relationship

class Branch(Base):

    __tablename__ = "branches"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    location = Column(String, nullable=False)

    inventories = relationship(
        "Inventory",
        back_populates="branch")