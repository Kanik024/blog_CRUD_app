from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def _get_validators_(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object ID")
        return ObjectId(v)

    @classmethod
    def _modify_schema_(cls, field_schema):
        field_schema.update(type="string")

class BlogPostCreate(BaseModel):
    title: str
    content: str
    author: str

class BlogPostUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
    author: Optional[str]

class BlogPostResponse(BaseModel):
    id: PyObjectId = Field(..., alias="_id")
    title: str
    content: str
    author: str
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        json_encoders = {ObjectId: str}

class CommentCreate(BaseModel):
    post_id: PyObjectId
    content: str
    author: str

class CommentResponse(BaseModel):
    id: PyObjectId = Field(..., alias="_id")
    post_id: PyObjectId
    content: str
    author: str
    created_at: datetime

    class Config:
        json_encoders = {ObjectId: str}

class LikeCreate(BaseModel):
    post_id: PyObjectId
    user: str

class LikeResponse(BaseModel):
    id: PyObjectId = Field(..., alias="_id")
    post_id: PyObjectId
    user: str

    class Config:
        json_encoders = {ObjectId: str}
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def _get_validators_(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object ID")
        return ObjectId(v)

    @classmethod
    def _modify_schema_(cls, field_schema):
        field_schema.update(type="string")

class BlogPostCreate(BaseModel):
    title: str
    content: str
    author: str

class BlogPostUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
    author: Optional[str]

class BlogPostResponse(BaseModel):
    id: PyObjectId = Field(..., alias="_id")
    title: str
    content: str
    author: str
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        json_encoders = {ObjectId: str}

class CommentCreate(BaseModel):
    post_id: PyObjectId
    content: str
    author: str

class CommentResponse(BaseModel):
    id: PyObjectId = Field(..., alias="_id")
    post_id: PyObjectId
    content: str
    author: str
    created_at: datetime

    class Config:
        json_encoders = {ObjectId: str}

class LikeCreate(BaseModel):
    post_id: PyObjectId
    user: str

class LikeResponse(BaseModel):
    id: PyObjectId = Field(..., alias="_id")
    post_id: PyObjectId
    user: str

    class Config:
        json_encoders = {ObjectId: str}
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def _get_validators_(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object ID")
        return ObjectId(v)

    @classmethod
    def _modify_schema_(cls, field_schema):
        field_schema.update(type="string")

class BlogPostCreate(BaseModel):
    title: str
    content: str
    author: str

class BlogPostUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
    author: Optional[str]

class BlogPostResponse(BaseModel):
    id: PyObjectId = Field(..., alias="_id")
    title: str
    content: str
    author: str
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        json_encoders = {ObjectId: str}

class CommentCreate(BaseModel):
    post_id: PyObjectId
    content: str
    author: str

class CommentResponse(BaseModel):
    id: PyObjectId = Field(..., alias="_id")
    post_id: PyObjectId
    content: str
    author: str
    created_at: datetime

    class Config:
        json_encoders = {ObjectId: str}

class LikeCreate(BaseModel):
    post_id: PyObjectId
    user: str

class LikeResponse(BaseModel):
    id: PyObjectId = Field(..., alias="_id")
    post_id: PyObjectId
    user: str

    class Config:
        json_encoders = {ObjectId: str}