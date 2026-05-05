from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.repositories.exhibition_repo import ExhibitionRepository
from app.schemas.exhibition import ExhibitionCreate, ExhibitionRead
from app.models.user import User
import uuid

class ExhibitionService:
    """Business logic for exhibition management"""
    def __init__(self, db: AsyncSession):
        self.repo = ExhibitionRepository(db)

    async def create_exhibition(self, exhibition_data: ExhibitionCreate, current_user: User) -> ExhibitionRead:
        """Create a new exhibition (admin only)"""
        if current_user.role != "admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admins can create exhibitions"
            )
        
        exhibition = await self.repo.create(exhibition_data)
        return ExhibitionRead.model_validate(exhibition)

    async def get_exhibition(self, exhibition_id: uuid.UUID) -> ExhibitionRead:
        """Get exhibition by ID"""
        exhibition = await self.repo.get_by_id(exhibition_id)
        if not exhibition:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Exhibition not found"
            )
        return ExhibitionRead.model_validate(exhibition)

    async def get_all_exhibitions(self, skip: int = 0, limit: int = 100) -> list[ExhibitionRead]:
        """Get all exhibitions"""
        exhibitions = await self.repo.get_all(skip, limit)
        return [ExhibitionRead.model_validate(e) for e in exhibitions]

    async def delete_exhibition(self, exhibition_id: uuid.UUID, current_user: User) -> dict:
        """Delete exhibition (admin only)"""
        if current_user.role != "admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admins can delete exhibitions"
            )
        
        deleted = await self.repo.delete(exhibition_id)
        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Exhibition not found"
            )
        return {"message": "Exhibition deleted successfully"}
