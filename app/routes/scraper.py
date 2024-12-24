from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def scrape_data():
    return {"message": "Hello from scraper"}