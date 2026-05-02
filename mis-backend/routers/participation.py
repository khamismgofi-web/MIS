#Participation endpoints
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependencies import get_db, get_current_user
from app.services.participation_service import ParticipationService
from app.schemas.participation import ParticipationCreate, ParticipationRead
from app.models.user import User
import uuid

router = APIRouter(prefix="/api/v1/participations", tags=["Participations"])

@router.post("/", response_model=ParticipationRead, status_code=201)
async def add_participant(
    data:         ParticipationCreate,
    db:           AsyncSession = Depends(get_db),
    current_user: User         = Depends(get_current_user),
):
    """Register a student or staff member as a participant on a project."""
    return await ParticipationService(db).add_participant(data, current_user)

@router.get("/project/{project_id}", response_model=list[ParticipationRead])
async def list_project_participants(
    project_id:   uuid.UUID,
    db:           AsyncSession = Depends(get_db),
    current_user: User         = Depends(get_current_user),
):
    """List all participants on a given project."""
    return await ParticipationService(db).get_project_participants(project_id)
@router.delete("/{user_id}/{project_id}", status_code=204)
async def remove_participant(
    user_id:      uuid.UUID,
    project_id:   uuid.UUID,
    db:           AsyncSession = Depends(get_db),
    current_user: User         = Depends(get_current_user),
):
    """Remove a participant from a project."""
    await ParticipationService(db).remove_participant(user_id, project_id, current_user)