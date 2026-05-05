from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.models.show_entry import ShowEntry
from app.schemas.show_entry import ShowEntryCreate
import uuid

class ShowEntryRepository:
    """Database operations for project-exhibition submissions"""
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, entry_data: ShowEntryCreate) -> ShowEntry | None:
        """Submit a project to an exhibition"""
        entry = ShowEntry(**entry_data.model_dump())
        self.db.add(entry)
        try:
            await self.db.flush()
        except IntegrityError:
            await self.db.rollback()
            return None  # Project already submitted to this exhibition
        await self.db.refresh(entry)
        return entry

    async def get_by_id(self, entry_id: uuid.UUID) -> ShowEntry | None:
        """Get show entry by ID"""
        result = await self.db.execute(
            select(ShowEntry).where(ShowEntry.id == entry_id)
        )
        return result.scalar_one_or_none()

    async def get_by_exhibition(self, exhibition_id: uuid.UUID) -> list[ShowEntry]:
        """Get all projects submitted to an exhibition"""
        result = await self.db.execute(
            select(ShowEntry).where(ShowEntry.exhibition_id == exhibition_id)
        )
        return list(result.scalars().all())

    async def get_by_project(self, project_id: uuid.UUID) -> list[ShowEntry]:
        """Get all exhibitions a project is submitted to"""
        result = await self.db.execute(
            select(ShowEntry).where(ShowEntry.project_id == project_id)
        )
        return list(result.scalars().all())

    async def update_status(self, entry_id: uuid.UUID, new_status: str) -> ShowEntry | None:
        """Update submission status"""
        entry = await self.get_by_id(entry_id)
        if not entry:
            return None
        entry.status = new_status
        await self.db.flush()
        await self.db.refresh(entry)
        return entry

    async def delete(self, entry_id: uuid.UUID) -> bool:
        """Delete a show entry"""
        entry = await self.get_by_id(entry_id)
        if not entry:
            return False
        await self.db.delete(entry)
        return True
