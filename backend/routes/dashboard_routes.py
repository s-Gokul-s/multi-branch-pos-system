from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.dashboard_schema import (
    DashboardStatsResponse,
    TopProductResponse,
    BranchSalesResponse
)

from services.dashboard_service import (
    get_dashboard_stats_service,
    get_top_products_service,
    get_branch_sales_service
)

from auth.auth_bearer import get_current_user
from auth.role_checker import admin_required


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/stats",
    response_model=DashboardStatsResponse
)
def get_dashboard_stats(

    current_user = Depends(get_current_user),

    db: Session = Depends(get_db)
):

    admin_required(current_user)

    return get_dashboard_stats_service(db)

@router.get(
    "/top-products",
    response_model=list[TopProductResponse]
)
def get_top_products(

    current_user = Depends(get_current_user),

    db: Session = Depends(get_db)
):

    admin_required(current_user)

    return get_top_products_service(db)


@router.get(
    "/branch-sales",
    response_model=list[BranchSalesResponse]
)
def get_branch_sales(

    current_user = Depends(get_current_user),

    db: Session = Depends(get_db)
):

    admin_required(current_user)

    return get_branch_sales_service(db)