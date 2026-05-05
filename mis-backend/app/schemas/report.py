from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime
from app.models.report import ReportType

class ReportRead(BaseModel):
    """Report data to send back from API"""
    id: UUID
    report_type: ReportType
    title: str
    content: str
    exhibition_id: Optional[UUID]
    generated_by_id: UUID
    generated_at: datetime

    class Config:
        from_attributes = True

class ReportSummary(BaseModel):
    """Summary of a report (brief version)"""
    id: UUID
    report_type: ReportType
    title: str
    generated_at: datetime