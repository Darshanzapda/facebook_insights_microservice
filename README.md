# Facebook Insights Microservice

## Overview
The **Facebook Insights Microservice** is a **FastAPI**-based application designed to scrape Facebook page insights, store the data in **MongoDB**, and expose REST APIs for easy access and usage. The service supports **GET** and **POST** operations for interacting with Facebook insights data.

## Features
- **FastAPI**: High-performance and easy-to-use backend framework.
- **MongoDB**: Efficient and scalable NoSQL database for storing insights.
- **REST APIs**:
  - **GET**: Retrieve insights data for a given Facebook page username.
  - **POST**: Scrape and store Facebook page insights by providing a username.
- **Scraped Data Includes:**
  - **Basic Page Details**:
    - ID
    - Username
    - Name
    - Page URL
    - Profile Picture
    - Category
    - Total Followers
    - Total Likes
  
---

## Installation
### Running Locally

#### 1. Clone the Repository
```bash
git clone https://github.com/Darshanzapda/facebook-insights-microservice.git
cd facebook-insights-microservice
```

#### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
# On Mac/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Set Up MongoDB
- Install MongoDB locally or use **MongoDB Atlas** for a cloud-based solution.
- **Use MongoDB Compass** for an easy-to-use GUI to manage and explore your MongoDB data.
- If using local MongoDB, start the server:
```bash
mongod --dbpath /data/db
```
- Verify MongoDB is running:
```bash
mongo
```

#### 5. Run the FastAPI Server
```bash
uvicorn app.main:app --reload
```

---

## API Usage

### **1. Scrape Facebook Insights** (Tested in Postman)
#### **POST** `/scrape`
To scrape and store Facebook page insights, send a **POST** request in **Postman** to:

**Endpoint:**
```http
http://127.0.0.1:8000/scrape
```

**Request Body (JSON):**
```json
{
  "username": "facebook_page_username"
}
```

---

### **2. Retrieve Insights for a Facebook Page** (Tested in Postman)
#### **GET** `/page/{username}`
To retrieve stored insights for a specific Facebook page, send a **GET** request in **Postman** to:

**Endpoint:**
```http
http://127.0.0.1:8000/page/{username}
```
Replace `{username}` with the actual Facebook page username.

---

## Postman Collection
A **Postman Collection JSON file** is attached to help with testing the API easily.

---

## Happy Coding! 🚀

