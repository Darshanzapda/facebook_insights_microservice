from fastapi import APIRouter, HTTPException
from pydantic import BaseModel 
from app.scraper import scrape_facebook_page
from app.database import db
from app.models import Page
from bson import ObjectId

# Pydantic model for the POST request body
class ScrapeRequest(BaseModel):
    username: str

# Convert MongoDB ObjectId to string
def mongo_objectid_to_str(data):
    if isinstance(data, dict):
        return {key: mongo_objectid_to_str(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [mongo_objectid_to_str(item) for item in data]
    elif isinstance(data, ObjectId):
        return str(data)
    return data

router = APIRouter()

@router.post("/scrape")
async def scrape_page(request: ScrapeRequest):
    username = request.username  # Get the username from the request body
    scraped_data = scrape_facebook_page(username)
    
    if not scraped_data:
        raise HTTPException(status_code=404, detail="Page not found or scraping failed")
    
    # Store the scraped data into MongoDB
    await db["pages"].insert_one(scraped_data)
    
    # Convert ObjectId to string for response
    scraped_data_str = mongo_objectid_to_str(scraped_data)
    
    return {"message": "Data scraped and saved successfully", "data": scraped_data_str}

@router.get("/page/{username}")
async def get_page_details(username: str):
    page_data = await db["pages"].find_one({"username": username})
    
    if not page_data:
        scraped_data = scrape_facebook_page(username)
        if not scraped_data:
            raise HTTPException(status_code=404, detail="Page not found")
        
        await db["pages"].insert_one(scraped_data)
        
        # Convert ObjectId to string for response
        scraped_data_str = mongo_objectid_to_str(scraped_data)
        return scraped_data_str
    
    # Convert ObjectId to string for response
    page_data_str = mongo_objectid_to_str(page_data)
    
    return page_data_str
