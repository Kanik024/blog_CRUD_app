from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import CommentCreate, CommentResponse
from app.crud import create_comment, get_comments, delete_comment
from app.models import Comment

router = APIRouter()

@router.post("/", response_model=CommentResponse)
async def create_comment_route(comment: CommentCreate):
    comment_model = Comment(**comment.dict())
    comment = await create_comment(comment_model)
    return comment

@router.get("/{post_id}", response_model=List[CommentResponse])
async def read_comments(post_id: str):
    comments = await get_comments(post_id)
    return comments

@router.delete("/{comment_id}", response_model=dict)
async def delete_comment_route(comment_id: str):
    success = await delete_comment(comment_id)
    if not success:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Comment deleted"}