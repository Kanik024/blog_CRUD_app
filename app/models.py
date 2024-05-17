from pydantic import BaseModel
from typing import List

class Post(BaseModel):
    title: str
    content: str
    author: str

class Comment(BaseModel):
    text: str
    author: str

class User(BaseModel):
    username: str
    email: str
