from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.repositories.user_repo import UserRepository
from app.schemas.users import UserCreate, UserUpdate, UserRead
from app.models.user import User

class UserService:
    """Business logic for user management"""
    def __init__(self, db: AsyncSession):
        self.repo = UserRepository(db)

    async def create_user(self, user_data: UserCreate) -> UserRead:
        """Create new user with validation"""
        # Check if email already exists
        existing = await self.repo.get_by_email(user_data.email)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )
        
        user = await self.repo.create(user_data)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to create user"
            )
        return UserRead.model_validate(user)

    async def get_user(self, user_id) -> UserRead:
        """Get user by ID"""
        user = await self.repo.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return UserRead.model_validate(user)

    async def get_all_users(self, skip: int = 0, limit: int = 100) -> list[UserRead]:
        """Get all users"""
        users = await self.repo.get_all(skip, limit)
        return [UserRead.model_validate(u) for u in users]

    async def update_user(self, user_id, user_data: UserUpdate, current_user: User) -> UserRead:
        """Update user (only admin or self)"""
        if current_user.role != "admin" and current_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized"
            )
        
        user = await self.repo.update(user_id, user_data)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return UserRead.model_validate(user)

    async def delete_user(self, user_id, current_user: User) -> dict:
        """Delete user (admin only)"""
        if current_user.role != "admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admins can delete users"
            )
        
        deleted = await self.repo.delete(user_id)
        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return {"message": "User deleted successfully"}
