from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from app.models.participation import ParticipationRole

class ParticipationCreate(BaseModel):
    """Data needed to add a user to a project"""
    user_id: UUID
    project_id: UUID
    role: ParticipationRole = ParticipationRole.MEMBER

class ParticipationRead(BaseModel):
    """Participation data to send back from API"""
    id: UUID
    user_id: UUID
    project_id: UUID
    role: ParticipationRole
    join_at: datetime

    class Config:
        from_attributes = True