from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependencies import get_db, get_current_user
from app.services.report_services import ReportService
from app.schemas.report import ReportRead
from app.models.user import User
import uuid

router = APIRouter(prefix="/api/v1/reports", tags=["Reports"])

@router.post("/", response_model=ReportRead, status_code=status.HTTP_201_CREATED)
async def generate_participation_report(
    exhibition_id: uuid.UUID | None = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Generate a participation report"""
    return await ReportService(db).generate_participation_report(exhibition_id, current_user)

@router.get("/{report_id}", response_model=ReportRead)
async def get_report(
    report_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get report by ID"""
    return await ReportService(db).get_report(report_id)

@router.get("/", response_model=list[ReportRead])
async def get_all_reports(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get all reports"""
    return await ReportService(db).get_all_reports(skip, limit)
