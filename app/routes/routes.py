from fastapi import APIRouter, HTTPException, Depends
from app.models import Post, Comment
from app.database import connect_to_mongo
from pymongo.collection import Collection

router = APIRouter()
db = connect_to_mongo()
posts_collection: Collection = db["posts"]

@router.post("/posts/")
async def create_post(post: Post):
    result = posts_collection.insert_one(post.dict())
    return {"id": str(result.inserted_id)}

@router.get("/posts/")
async def get_posts():
    posts = []
    for post in posts_collection.find():
        posts.append(Post(**post))
    return posts

@router.get("/posts/{post_id}")
async def get_post(post_id: str):
    post = posts_collection.find_one({"_id": post_id})
    if post:
        return Post(**post)
    else:
        raise HTTPException(status_code=404, detail="Post not found")

@router.put("/posts/{post_id}")
async def update_post(post_id: str, post: Post):
    result = posts_collection.update_one({"_id": post_id}, {"$set": post.dict()})
    if result.modified_count == 1:
        return {"message": "Post updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")

@router.delete("/posts/{post_id}")
async def delete_post(post_id: str):
    result = posts_collection.delete_one({"_id": post_id})
    if result.deleted_count == 1:
        return {"message": "Post deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")
