from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# User Schemas
class UserCreate(BaseModel):
    email : EmailStr
    password: str = Field(min_length=6, max_length=72)

class TokenResponse(BaseModel):
    access_token : str
    token_type : str

# Task Schemas
class TaskCreate(BaseModel):
    title : str = Field(..., min_length=1)

class TaskResponse(BaseModel):
    id : int
    title : str
    completed : bool

    class Config:
        from_attributes = True

class TaskUpdate(BaseModel):
    title : Optional[str] = Field(None, min_length=1)
    completed : Optional[bool] = None

