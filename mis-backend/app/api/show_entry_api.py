from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependencies import get_db, get_current_user
from app.repositories.show_entry_repo import ShowEntryRepository
from app.schemas.show_entry import ShowEntryCreate, ShowEntryRead
from app.models.user import User
import uuid

router = APIRouter(prefix="/api/v1/show-entries", tags=["ShowEntries"])

@router.post("/", response_model=ShowEntryRead, status_code=status.HTTP_201_CREATED)
async def submit_project_to_exhibition(
    entry_data: ShowEntryCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Submit a project to an exhibition"""
    repo = ShowEntryRepository(db)
    entry = await repo.create(entry_data)
    if not entry:
        return {"detail": "Project already submitted to this exhibition"}
    return ShowEntryRead.model_validate(entry)

@router.get("/{entry_id}", response_model=ShowEntryRead)
async def get_show_entry(
    entry_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get show entry by ID"""
    repo = ShowEntryRepository(db)
    entry = await repo.get_by_id(entry_id)
    if not entry:
        return {"detail": "Show entry not found"}
    return ShowEntryRead.model_validate(entry)

@router.get("/exhibition/{exhibition_id}", response_model=list[ShowEntryRead])
async def list_exhibition_entries(
    exhibition_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get all projects submitted to an exhibition"""
    repo = ShowEntryRepository(db)
    entries = await repo.get_by_exhibition(exhibition_id)
    return [ShowEntryRead.model_validate(e) for e in entries]

@router.get("/project/{project_id}", response_model=list[ShowEntryRead])
async def list_project_exhibitions(
    project_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get all exhibitions a project is submitted to"""
    repo = ShowEntryRepository(db)
    entries = await repo.get_by_project(project_id)
    return [ShowEntryRead.model_validate(e) for e in entries]

@router.delete("/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_show_entry(
    entry_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Delete/withdraw a show entry"""
    repo = ShowEntryRepository(db)
    await repo.delete(entry_id)
