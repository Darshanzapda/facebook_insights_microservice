from pydantic import BaseModel
from typing import List, Optional

class Page(BaseModel):
    username: str
    name: str
    url: str
    id: str
    profile_pic: Optional[str]
    email: Optional[str]
    website: Optional[str]
    category: Optional[str]
    total_followers: int
    total_likes: int
    created_at: str
    posts: List[str] = []

class Post(BaseModel):
    post_id: str
    content: Optional[str]
    likes: int
    comments: int
    timestamp: str

class Follower(BaseModel):
    id: str
    name: str
    profile_pic: Optional[str]
