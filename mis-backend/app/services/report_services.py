#Report generation logic
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from fastapi import HTTPException
from app.models.participation import Participation
from app.models.project import Project
from app.models.show_entry import ShowEntry
from app.models.report import Report, ReportType
from app.models.user import User
import uuid, json

class ReportService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def generate_participation_report(
        self, exhibition_id: uuid.UUID | None, admin: User
    ) -> Report:
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