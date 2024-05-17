from fastapi import APIRouter, HTTPException
from app.schemas import LikeCreate, LikeResponse
from app.crud import create_like, delete_like
from app.models import Like

router = APIRouter()

@router.post("/", response_model=LikeResponse)
async def like_post(like: LikeCreate):
    like_model = Like(**like.dict())
    like = await create_like(like_model)
    return like

@router.delete("/{like_id}", response_model=dict)
async def unlike_post(like_id: str):
    success = await delete_like(like_id)
    if not success:
        raise HTTPException(status_code=404, detail="Like not found")
    return {"message": "Like removed"}