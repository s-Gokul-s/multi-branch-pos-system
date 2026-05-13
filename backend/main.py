from fastapi import FastAPI
from database import engine
from database import Base

from models.products import Product
from models.user import User
from models.branch import Branch
from models.inventory import Inventory
from routes.product_routes import router as product_router
from routes.auth_routes import router as auth_router
from routes.branch_routes import router as branch_router
from routes.inventory_routes import router as inventory_router


app = FastAPI()


app.include_router(product_router)
app.include_router(auth_router)
app.include_router(branch_router)
app.include_router(inventory_router)




@app.get("/")
def home():
    return {"message": "POS SYSTEM RUNNING BACKGROUND"}
