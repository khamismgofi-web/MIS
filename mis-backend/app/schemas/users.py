from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime
from app.models.user import UserRole

class UserCreate(BaseModel):
    """Data needed to create a new user"""
    full_name: str
    email: EmailStr
    password: str
    role: UserRole = UserRole.STUDENT
    department: Optional[str] = None

class UserUpdate(BaseModel):
    """Data that can be updated on a user"""
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    department: Optional[str] = None
    is_active: Optional[bool] = None

class UserRead(BaseModel):
    """User data to send back from API"""
    id: UUID
    full_name: str
    email: str
    role: UserRole
    department: Optional[str]
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True