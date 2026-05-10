from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name : str
    category : str
    price : float = Field(gt=0)
    barcode : str




class ProductResponse(BaseModel):
    name : str
    category : str
    price : float = Field(gt=0)
    barcode : str


    class Config:
        from_attributes = True


class ProductUpdate(BaseModel):

    name: str
    category: str
    price: float = Field(gt=0)
    barcode: str