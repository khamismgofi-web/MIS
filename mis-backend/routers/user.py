#User CRUD endpoints
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependencies import get_db, get_current_user
from app.services.user_services import UserService
from app.schemas.users import UserCreate, UserRead, UserUpdate
from app.models.user import User
import uuid

router = APIRouter(prefix="/api/v1/users", tags=["Users"])

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    """Create a new user"""
    return await UserService(db).create_user(user_data)

@router.get("/{user_id}", response_model=UserRead)
async def get_user(
    user_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get user by ID"""
    return await UserService(db).get_user(user_id)

@router.get("/", response_model=list[UserRead])
async def get_all_users(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get all users"""
    return await UserService(db).get_all_users(skip, limit)

@router.put("/{user_id}", response_model=UserRead)
async def update_user(
    user_id: uuid.UUID,
    user_data: UserUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Update user"""
    return await UserService(db).update_user(user_id, user_data, current_user)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Delete user"""
    await UserService(db).delete_user(user_id, current_user)
