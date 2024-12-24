from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Cart

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.get("/")
def get_cart(db: Session = Depends(get_db)):
    return db.query(Cart).all()

@router.post("/")
def add_to_cart(item_id: int, quantity: int, db: Session = Depends(get_db)):
    cart_item = Cart(item_id=item_id, quantity=quantity)
    db.add(cart_item)
    db.commit()
    return {"message": "Item added to cart successfully!"}