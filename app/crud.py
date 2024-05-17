from typing import List, Optional
from app.models import BlogPost, Comment, Like
from app.schemas import BlogPostCreate, BlogPostUpdate
from app.database import db
from bson import ObjectId
from datetime import datetime

async def create_blog_post(post: BlogPostCreate) -> BlogPost:
    blog_post = BlogPost(**post.dict())
    await db.database.blog_posts.insert_one(blog_post.dict())
    return blog_post

async def get_blog_post(id: str) -> Optional[BlogPost]:
    post = await db.database.blog_posts.find_one({"_id": ObjectId(id)})
    if post:
        return BlogPost(**post)

async def update_blog_post(id: str, post: BlogPostUpdate) -> Optional[BlogPost]:
    update_data = {k: v for k, v in post.dict().items() if v is not None}
    update_data["updated_at"] = datetime.utcnow()
    updated_post = await db.database.blog_posts.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": update_data},
        return_document=True
    )
    if updated_post:
        return BlogPost(**updated_post)

async def delete_blog_post(id: str) -> bool:
    result = await db.database.blog_posts.delete_one({"_id": ObjectId(id)})
    return result.deleted_count == 1

async def get_all_blog_posts() -> List[BlogPost]:
    posts = []
    async for post in db.database.blog_posts.find():
        posts.append(BlogPost(**post))
    return posts

async def create_comment(comment: Comment) -> Comment:
    await db.database.comments.insert_one(comment.dict())
    return comment

async def get_comments(post_id: str) -> List[Comment]:
    comments = []
    async for comment in db.database.comments.find({"post_id": ObjectId(post_id)}):
        comments.append(Comment(**comment))
    return comments

async def delete_comment(comment_id: str) -> bool:
    result = await db.database.comments.delete_one({"_id": ObjectId(comment_id)})
    return result.deleted_count == 1

async def create_like(like: Like) -> Like:
    await db.database.likes.insert_one(like.dict())
    return like

async def delete_like(like_id: str) -> bool:
    result = await db.database.likes.delete_one({"_id": ObjectId(like_id)})
    return result.deleted_count == 1