#Exhibition CRUD endpoints
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependencies import get_db, get_current_user
from app.services.exhibition_services import ExhibitionService
from app.schemas.exhibition import ExhibitionCreate, ExhibitionRead
from app.models.user import User
import uuid

router = APIRouter(prefix="/api/v1/exhibitions", tags=["Exhibitions"])

@router.post("/", response_model=ExhibitionRead, status_code=status.HTTP_201_CREATED)
async def create_exhibition(
    exhibition_data: ExhibitionCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create a new exhibition"""
    return await ExhibitionService(db).create_exhibition(exhibition_data, current_user)

@router.get("/{exhibition_id}", response_model=ExhibitionRead)
async def get_exhibition(
    exhibition_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get exhibition by ID"""
    return await ExhibitionService(db).get_exhibition(exhibition_id)

@router.get("/", response_model=list[ExhibitionRead])
async def get_all_exhibitions(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get all exhibitions"""
    return await ExhibitionService(db).get_all_exhibitions(skip, limit)

@router.delete("/{exhibition_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_exhibition(
    exhibition_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Delete exhibition"""
    await ExhibitionService(db).delete_exhibition(exhibition_id, current_user)
