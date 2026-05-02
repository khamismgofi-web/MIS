#Participation Rules
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.repositories.participation_repo import ParticipationRepository
from app.repositories.project_repo import ProjectRepository
from app.schemas.participation import ParticipationCreate, ParticipationRead
from app.models.user import User
import uuid

class ParticipationService:
    def __init__(self, db: AsyncSession):
        self.repo         = ParticipationRepository(db)
        self.project_repo = ProjectRepository(db)

    async def add_participant(
        self, data: ParticipationCreate, current_user: User
    ) -> ParticipationRead:
        # Business rule 1: project must exist
        project = await self.project_repo.get_by_id(data.project_id)
        if not project:
            raise HTTPException(status_code=404, detail='Project not found')

        # Business rule 2: student cannot join a REJECTED project
        if project.status == 'rejected':
            raise HTTPException(status_code=400, detail='Cannot join a rejected project')

        # Attempt to add (repo returns None on duplicate)
        result = await self.repo.add(data)
        if result is None:
            raise HTTPException(status_code=409, detail='User already participating in this project')
        return ParticipationRead.model_validate(result)

    async def get_project_participants(
        self, project_id: uuid.UUID
    ) -> list[ParticipationRead]:
        entries = await self.repo.get_by_project(project_id)
        return [ParticipationRead.model_validate(e) for e in entries]

    async def remove_participant(
        self, user_id: uuid.UUID, project_id: uuid.UUID, current_user: User
    ):
        # Business rule: only admin or the user themselves can remove
        if current_user.role != 'admin' and current_user.id != user_id:
            raise HTTPException(status_code=403, detail='Not authorized')
        removed = await self.repo.remove(user_id, project_id)
        if not removed:
            raise HTTPException(status_code=404, detail='Participation record not found')
        return {"message": "Participant removed successfully"}