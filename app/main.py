from fastapi import FastAPI
from app.routes import blog_posts, comments, likes
import motor.motor_asyncio
from app.database import db

app = FastAPI()

app.include_router(blog_posts.router, prefix="/posts", tags=["Blog Posts"])
app.include_router(comments.router, prefix="/comments", tags=["Comments"])
app.include_router(likes.router, prefix="/likes", tags=["Likes"])

@app.on_event("startup")
async def startup_db_client():
    db.client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
    db.database = db.client.blog_api

@app.on_event("shutdown")
async def shutdown_db_client():
    db.client.close()