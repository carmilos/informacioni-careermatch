from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    is_hr: Optional[bool] = False

class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_hr: bool
    class Config:
        orm_mode = True

class JobCreate(BaseModel):
    title: str
    company: Optional[str] = ''
    location: Optional[str] = ''
    description: Optional[str] = ''

class JobOut(BaseModel):
    id: int
    title: str
    company: Optional[str]
    location: Optional[str]
    description: Optional[str]
    owner_id: Optional[int]
    created_at: datetime
    class Config:
        orm_mode = True

class ApplicantCreate(BaseModel):
    name: str
    email: EmailStr

class ApplicantOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    cv_path: str
    applied_at: datetime
    class Config:
        orm_mode = True
