from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import BlogPostCreate, BlogPostUpdate, BlogPostResponse
from app.crud import create_blog_post, get_blog_post, update_blog_post, delete_blog_post, get_all_blog_posts

router = APIRouter()

@router.post("/", response_model=BlogPostResponse)
async def create_post(post: BlogPostCreate):
    blog_post = await create_blog_post(post)
    return blog_post

@router.get("/{id}", response_model=BlogPostResponse)
async def read_post(id: str):
    blog_post = await get_blog_post(id)
    if not blog_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return blog_post

@router.put("/{id}", response_model=BlogPostResponse)
async def update_post(id: str, post: BlogPostUpdate):
    updated_post = await update_blog_post(id, post)
    if not updated_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post

@router.delete("/{id}", response_model=dict)
async def delete_post(id: str):
    success = await delete_blog_post(id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted"}

@router.get("/", response_model=List[BlogPostResponse])
async def read_all_posts():
    posts = await get_all_blog_posts()
    return posts