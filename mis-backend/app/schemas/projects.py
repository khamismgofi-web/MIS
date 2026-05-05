from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime
from app.models.project import ProjectCategory, ProjectStatus

class ProjectCreate(BaseModel):
    """Data needed to create a new project"""
    title: str
    description: str
    category: ProjectCategory = ProjectCategory.OTHER
    supervisor_id: Optional[UUID] = None

class ProjectUpdate(BaseModel):
    """Data that can be updated on a project"""
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[ProjectCategory] = None
    status: Optional[ProjectStatus] = None
    supervisor_id: Optional[UUID] = None

class ProjectRead(BaseModel):
    """Project data to send back from API"""
    id: UUID
    title: str
    description: str
    category: ProjectCategory
    status: ProjectStatus
    supervisor_id: Optional[UUID]
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True