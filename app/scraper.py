from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup
import logging
import os

# Initialize logging for better error reporting
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scrape_facebook_page(username):
    url = f"https://www.facebook.com/{username}"
    
    # Setup Selenium WebDriver for dynamic content scraping
    options = Options()
    options.add_argument("--headless")  # Run in headless mode to avoid opening a browser window

    # Specify the path to chromedriver.exe (update this path accordingly)
    chromedriver_path = r"C:\Windows\chromedriver.exe"  # Modify this path if necessary
    if not os.path.exists(chromedriver_path):
        logger.error(f"ChromeDriver not found at {chromedriver_path}")
        return {"message": "ChromeDriver not found", "detail": f"Please check the path: {chromedriver_path}"}

    service = Service(chromedriver_path)  # Provide the correct chromedriver path
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(url)
        
        # Wait for specific elements to load before scraping
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//meta[@property='og:title']"))
        )
        
        # Scrape the page source
        page_source = driver.page_source
        
        # Parse page source with BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')
        
        # Extract page details
        page_name = soup.find("meta", property="og:title")["content"] if soup.find("meta", property="og:title") else "N/A"
        profile_pic = soup.find("meta", property="og:image")["content"] if soup.find("meta", property="og:image") else "N/A"
        category = soup.find("meta", property="og:description")["content"] if soup.find("meta", property="og:description") else "N/A"

        # Scrape followers count
        total_followers = "Not available"
        total_likes = "Not available"
        
        try:
            # Wait for the followers link to load
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/followers/')]"))
            )
            followers_section = driver.find_element(By.XPATH, "//a[contains(@href, '/followers/')]")
            total_followers = followers_section.text.strip()
            logger.info(f"Followers: {total_followers}")
            
            # Similarly scrape the likes
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/friends_likes/')]"))
            )
            likes_section = driver.find_element(By.XPATH, "//a[contains(@href, '/friends_likes/')]")
            total_likes = likes_section.text.strip()
            logger.info(f"Likes: {total_likes}")
            
        except Exception as e:
            logger.error(f"Error scraping followers/likes: {e}")
            total_followers = total_likes = "Not available"

        # Return the scraped data without the posts field
        return {
            "username": username,
            "name": page_name,
            "url": url,
            "profile_pic": profile_pic,
            "category": category,
            "total_followers": total_followers,
            "total_likes": total_likes
        }
    
    except Exception as e:
        logger.error(f"Error scraping page for {username}: {e}")
        return {
            "message": "Page not found or scraping failed",
            "detail": str(e)
        }
    finally:
        driver.quit()

# Example usage:
if __name__ == "__main__":
    username = "boat.lifestyle"  # Replace with the Facebook page username you want to scrape
    scraped_data = scrape_facebook_page(username)
    print(scraped_data)
