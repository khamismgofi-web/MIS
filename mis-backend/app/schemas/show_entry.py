from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime
from app.models.show_entry import EntryStatus

class ShowEntryCreate(BaseModel):
    """Data needed to submit a project to an exhibition"""
    project_id: UUID
    exhibition_id: UUID
    notes: Optional[str] = None

class ShowEntryRead(BaseModel):
    """Show entry data to send back from API"""
    id: UUID
    project_id: UUID
    exhibition_id: UUID
    status: EntryStatus
    notes: Optional[str]
    submitted_at: datetime

    class Config:
        from_attributes = True