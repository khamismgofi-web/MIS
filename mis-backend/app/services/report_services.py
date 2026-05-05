#Report generation logic
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from fastapi import HTTPException, status
from app.repositories.report_repo import ReportRepository
from app.models.participation import Participation
from app.models.project import Project
from app.models.show_entry import ShowEntry
from app.models.report import Report, ReportType
from app.models.user import User
import uuid, json

class ReportService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repo = ReportRepository(db)

    async def generate_participation_report(
        self, exhibition_id: uuid.UUID | None, admin: User
    ) -> Report:
        """Generate a report showing who participated in which project"""
        # Count participants per project
        result = await self.db.execute(
            select(Project.title, func.count(Participation.id).label('count'))
            .join(Participation, Project.id == Participation.project_id)
            .group_by(Project.id)
        )
        rows = result.all()
        summary = {row.title: row.count for row in rows}

        report = Report(
            report_type=ReportType.PARTICIPATION,
            title=f"Participation Report — {len(rows)} projects",
            content=json.dumps(summary, indent=2),
            exhibition_id=exhibition_id,
            generated_by_id=admin.id,
        )
        self.db.add(report)
        await self.db.flush()
        await self.db.refresh(report)
        return report

    async def get_report(self, report_id: uuid.UUID) -> Report:
        """Get report by ID"""
        report = await self.repo.get_by_id(report_id)
        if not report:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Report not found"
            )
        return report

    async def get_all_reports(self, skip: int = 0, limit: int = 100) -> list[Report]:
        """Get all reports"""
        return await self.repo.get_all(skip, limit)
