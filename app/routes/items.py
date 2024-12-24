from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Item

router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/")
def get_items(db: Session = Depends(get_db)):
    return db.query(Item).all()

@router.post("/")
def add_items(name: str, price: float, store_id: int, db:Session=Depends(get_db)):
    item= Item(name=name, price=price, store_id=store_id)
    db.add(item)
    db.commit()
    return {"message": "Item added successfully!"}