from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.models.exhibition import Exhibition
from app.schemas.exhibition import ExhibitionCreate
import uuid

class ExhibitionRepository:
    """Database operations for exhibitions"""
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, exhibition_data: ExhibitionCreate) -> Exhibition:
        """Create a new exhibition"""
        exhibition = Exhibition(
            name=exhibition_data.name,
            description=exhibition_data.description,
            venue=exhibition_data.venue,
            event_date=exhibition_data.event_date
        )
        self.db.add(exhibition)
        await self.db.flush()
        await self.db.refresh(exhibition)
        return exhibition

    async def get_by_id(self, exhibition_id: uuid.UUID) -> Exhibition | None:
        """Get exhibition by ID"""
        result = await self.db.execute(
            select(Exhibition).where(Exhibition.id == exhibition_id)
        )
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 100) -> list[Exhibition]:
        """Get all exhibitions"""
        result = await self.db.execute(
            select(Exhibition).offset(skip).limit(limit)
        )
        return list(result.scalars().all())

    async def delete(self, exhibition_id: uuid.UUID) -> bool:
        """Delete an exhibition"""
        exhibition = await self.get_by_id(exhibition_id)
        if not exhibition:
            return False
        await self.db.delete(exhibition)
        return True
