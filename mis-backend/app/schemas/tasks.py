from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class TaskCreate(BaseModel):
    """Data needed to create a task"""
    title: str
    description: Optional[str] = None
    project_id: UUID
    assigned_to: Optional[UUID] = None

class TaskRead(BaseModel):
    """Task data to send back from API"""
    id: UUID
    title: str
    description: Optional[str]
    project_id: UUID
    assigned_to: Optional[UUID]

    class Config:
        from_attributes = True
