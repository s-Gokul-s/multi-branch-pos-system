from pydantic import BaseModel, Field

from schemas.product_schema import ProductResponse

from schemas.branch_schema import BranchResponse

class InventoryCreate(BaseModel):

    branch_id: int

    product_id: int

    stock: int = Field(ge=0)


class InventoryResponse(BaseModel):

    id: int

    branch_id: int

    product_id: int

    stock: int

    class Config:
        from_attributes = True



class InventoryUpdate(BaseModel):

    stock: int = Field(ge=0)



class InventoryDetailedResponse(BaseModel):

    id: int

    stock: int

    product: ProductResponse

    branch: BranchResponse

    class Config:
        from_attributes = True