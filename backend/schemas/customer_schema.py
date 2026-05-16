from pydantic import BaseModel


class CustomerCreate(BaseModel):

    name: str

    phone: str


class CustomerResponse(BaseModel):

    id: int

    name: str

    phone: str

    loyalty_points: int

    class Config:
        from_attributes = True