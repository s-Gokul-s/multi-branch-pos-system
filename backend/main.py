from fastapi import FastAPI
from database import engine
from database import Base

from models.products import Product
from routes.product_routes import router as product_router

app = FastAPI()


app.include_router(product_router)

Base.metadata.create_all(bind = engine)


@app.get("/")
def home():
    return {"message": "POS SYSTEM RUNNING BACKGROUND"}
