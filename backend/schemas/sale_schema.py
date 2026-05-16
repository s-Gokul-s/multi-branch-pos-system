from pydantic import BaseModel, Field

from schemas.product_schema import ProductResponse

class SaleItemCreate(BaseModel):

    product_id: int

    quantity: int = Field(gt=0)


class SaleCreate(BaseModel):

    customer_id: int | None = None

    items: list[SaleItemCreate]


class SaleItemResponse(BaseModel):

    product: ProductResponse

    
    quantity: int

    price: float

    subtotal: float

    class Config:
        from_attributes = True


class SaleResponse(BaseModel):

    id: int

    total_amount: float

    items: list[SaleItemResponse]

    class Config:
        from_attributes = True