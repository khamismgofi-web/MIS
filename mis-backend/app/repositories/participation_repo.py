from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.models.participation import Participation
from app.schemas.participation import ParticipationCreate
import uuid

class ParticipationRepository:
    """Database operations for user-project participation"""
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add(self, data: ParticipationCreate) -> Participation | None:
        """Add a user to a project"""
        entry = Participation(**data.model_dump())
        self.db.add(entry)
        try:
            await self.db.flush()
        except IntegrityError:
            await self.db.rollback()
            return None  # User already in project
        await self.db.refresh(entry)
        return entry

    async def get_by_id(self, participation_id: uuid.UUID) -> Participation | None:
        """Get participation by ID"""
        result = await self.db.execute(
            select(Participation).where(Participation.id == participation_id)
        )
        return result.scalar_one_or_none()

    async def get_by_project(self, project_id: uuid.UUID) -> list[Participation]:
        """Get all participants in a project"""
        result = await self.db.execute(
            select(Participation)
            .where(Participation.project_id == project_id)
            .order_by(Participation.join_at)
        )
        return list(result.scalars().all())

    async def get_by_user(self, user_id: uuid.UUID) -> list[Participation]:
        """Get all projects a user participates in"""
        result = await self.db.execute(
            select(Participation).where(Participation.user_id == user_id)
        )
        return list(result.scalars().all())

    async def remove(self, user_id: uuid.UUID, project_id: uuid.UUID) -> bool:
        """Remove a user from a project"""
        result = await self.db.execute(
            select(Participation)
            .where(Participation.user_id == user_id)
            .where(Participation.project_id == project_id)
        )
        entry = result.scalar_one_or_none()
        if not entry:
            return False
        await self.db.delete(entry)
        return True
