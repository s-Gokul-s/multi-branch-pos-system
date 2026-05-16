from pydantic import BaseModel


class DashboardStatsResponse(BaseModel):

    total_sales: float

    total_products: int

    total_branches: int

    low_stock_count: int



class TopProductResponse(BaseModel):

    product_name: str

    total_quantity: int

class BranchSalesResponse(BaseModel):

    branch_name: str

    total_sales: float

