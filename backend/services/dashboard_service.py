from sqlalchemy.orm import Session

from sqlalchemy import func

from models.sale import Sale
from models.sale_item import SaleItem
from models.products import Product
from models.branch import Branch
from models.inventory import Inventory


def get_dashboard_stats_service(db: Session):
    total_sales = db.query(
        func.coalesce(func.sum(Sale.total_amount), 0)
    ).scalar()

    total_products = db.query(Product).count()

    total_branches = db.query(Branch).count()

    low_stock_count = db.query(Inventory).filter(
        Inventory.stock < 10
    ).count()

    return {
        "total_sales": total_sales,
        "total_products": total_products,
        "total_branches": total_branches,
        "low_stock_count": low_stock_count
    }


def get_top_products_service(db: Session):
    results = db.query(

        Product.name.label("product_name"),

        func.sum(SaleItem.quantity).label(
            "total_quantity"
        )

    ).join(
        SaleItem,
        Product.id == SaleItem.product_id
    ).group_by(
        Product.name
    ).order_by(
        func.sum(SaleItem.quantity).desc()
    ).limit(5).all()

    return [
        {
            "product_name": r.product_name,
            "total_quantity": r.total_quantity
        }
        for r in results
    ]

def get_branch_sales_service(db: Session):

    results = db.query(

        Branch.name.label("branch_name"),

        func.sum(Sale.total_amount).label(
            "total_sales"
        )

    ).join(
        Sale,
        Branch.id == Sale.branch_id
    ).group_by(
        Branch.name
    ).all()

    return [
        {
            "branch_name": r.branch_name,
            "total_sales": r.total_sales
        }
        for r in results
    ]