from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL="postgresql://postgres:0000@localhost:5432/grocery_price_tracker"

engine=create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_connection():
    try:
        with engine.connect() as connection:
            print("Connected to postgreSQL successfully")
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")