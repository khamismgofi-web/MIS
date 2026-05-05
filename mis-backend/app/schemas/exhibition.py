from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import date, datetime
from app.models.exhibition import ExhibitionStatus

class ExhibitionCreate(BaseModel):
    """Data needed to create a new exhibition"""
    name: str
    description: Optional[str] = None
    venue: Optional[str] = None
    event_date: date

class ExhibitionRead(BaseModel):
    """Exhibition data to send back from API"""
    id: UUID
    name: str
    description: Optional[str]
    venue: Optional[str]
    event_date: date
    status: ExhibitionStatus
    created_at: datetime

    class Config:
        from_attributes = True