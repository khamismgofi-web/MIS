from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependencies import get_db, get_current_user
from app.services.project_services import ProjectService
from app.schemas.projects import ProjectCreate, ProjectRead, ProjectUpdate
from app.models.user import User
import uuid

router = APIRouter(prefix="/api/v1/projects", tags=["Projects"])

@router.post("/", response_model=ProjectRead, status_code=status.HTTP_201_CREATED)
async def create_project(
    project_data: ProjectCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create a new project"""
    return await ProjectService(db).create_project(project_data, current_user)

@router.get("/{project_id}", response_model=ProjectRead)
async def get_project(
    project_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get project by ID"""
    return await ProjectService(db).get_project(project_id)

@router.get("/", response_model=list[ProjectRead])
async def get_all_projects(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get all projects"""
    return await ProjectService(db).get_all_projects(skip, limit)

@router.put("/{project_id}", response_model=ProjectRead)
async def update_project(
    project_id: uuid.UUID,
    project_data: ProjectUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Update project"""
    return await ProjectService(db).update_project(project_id, project_data, current_user)

@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(
    project_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Delete project"""
    await ProjectService(db).delete_project(project_id, current_user)
