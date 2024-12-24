from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Store(Base):
    __tablename__= "stores"
    id= Column(Integer,primary_key=True,index=True)
    name=Column(String, unique=True, index=True)

class Item(Base):
    __tablename__= "items"
    id= Column(Integer, primary_key=True, index=True)
    name= Column(String, index=True)
    price= Column(Float)
    store_id= Column(Integer, ForeignKey("stores.id"))
    store= relationship("Store")

class Cart(Base):
    __tablename__= "carts"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    quantity=Column(Integer)
    item=relationship("Item")