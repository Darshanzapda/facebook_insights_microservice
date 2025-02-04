from app.database import db
from app.models import FacebookPage
import requests
from bs4 import BeautifulSoup

# Function to scrape the Facebook page details
def scrape_facebook_page(username: str):
    url = f"https://www.facebook.com/{username}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract page details
    page_data = {
        "username": username,
        "name": soup.find("meta", {"property": "og:title"})["content"],
        "url": url,
        "profile_pic": soup.find("meta", {"property": "og:image"})["content"],
        "category": "Social Media",
        "total_followers": 5000,  # You would scrape real data here
    }

    # Store in DB
    page = FacebookPage(**page_data)
    db.pages.insert_one(page.dict())

    return page_data
