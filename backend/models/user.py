from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base



class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index =True)

    name = Column(String, nullable = False)

    email = Column(String, unique=True, nullable=False)

    password = Column(String, nullable=False)

    role = Column(String, nullable=False)

    branch_id = Column(
                Integer,
                ForeignKey("branches.id"),
                nullable=True
            )