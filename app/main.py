from fastapi import FastAPI
from app.routes import items,cart,scraper
from app.database import engine, Base

app= FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(items.router, prefix="/items", tags=["Items"])
app.include_router(cart.router, prefix="/cart", tags=["Cart"])
app.include_router(scraper.router, prefix="/scraper", tags=["Scraper"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Grocery Price Tracker API"}