from fastapi import FastAPI
from database import engine
from database import Base

from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from logger import logger


from models.products import Product
from models.user import User
from models.branch import Branch
from models.inventory import Inventory
from models.sale import Sale
from models.sale_item import SaleItem
from models.customer import Customer


from routes.product_routes import router as product_router
from routes.auth_routes import router as auth_router
from routes.branch_routes import router as branch_router
from routes.inventory_routes import router as inventory_router
from routes.sale_routes import router as sale_router
from routes.customer_routes import router as customer_router
from routes.dashboard_routes import router as dashboard_router


app = FastAPI()

@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):

    logger.error(
        f"Unhandled Error: {str(exc)}"
    )

    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal Server Error"
        }
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):

    logger.warning(
        f"Validation Error: {exc.errors()}"
    )

    return JSONResponse(
        status_code=422,
        content={
            "detail": exc.errors()
        }
    )


app.include_router(product_router)
app.include_router(auth_router)
app.include_router(branch_router)
app.include_router(inventory_router)
app.include_router(sale_router)
app.include_router(customer_router)
app.include_router(dashboard_router)


@app.get("/")
def home():
    return {"message": "POS SYSTEM RUNNING BACKGROUND"}
