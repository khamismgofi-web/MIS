#ParticipationDB querries
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.models.participation import Participation
from app.schemas.participation import ParticipationCreate
import uuid

class ParticipationRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add(self, data: ParticipationCreate) -> Participation:
        entry = Participation(**data.model_dump())
        self.db.add(entry)
        try:
            await self.db.flush()
        except IntegrityError:
            await self.db.rollback()
            return None   # signals duplicate to the service layer
        await self.db.refresh(entry)
        return entry

    async def get_by_project(self, project_id: uuid.UUID) -> list[Participation]:
        result = await self.db.execute(
            select(Participation)
            .where(Participation.project_id == project_id)
            .order_by(Participation.joined_at)
        )
        return list(result.scalars().all())