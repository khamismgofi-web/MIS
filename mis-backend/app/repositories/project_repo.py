from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.models.project import Project, ProjectStatus
from app.schemas.projects import ProjectCreate, ProjectUpdate
import uuid

class ProjectRepository:
    """Database operations for projects"""
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, project_data: ProjectCreate) -> Project:
        """Create a new project"""
        project = Project(
            title=project_data.title,
            description=project_data.description,
            category=project_data.category,
            supervisor_id=project_data.supervisor_id
        )
        self.db.add(project)
        await self.db.flush()
        await self.db.refresh(project)
        return project

    async def get_by_id(self, project_id: uuid.UUID) -> Project | None:
        """Get project by ID"""
        result = await self.db.execute(
            select(Project).where(Project.id == project_id)
        )
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 100) -> list[Project]:
        """Get all projects"""
        result = await self.db.execute(
            select(Project).offset(skip).limit(limit)
        )
        return list(result.scalars().all())

    async def get_by_supervisor(self, supervisor_id: uuid.UUID) -> list[Project]:
        """Get all projects supervised by a user"""
        result = await self.db.execute(
            select(Project).where(Project.supervisor_id == supervisor_id)
        )
        return list(result.scalars().all())

    async def update(self, project_id: uuid.UUID, project_data: ProjectUpdate) -> Project | None:
        """Update a project"""
        project = await self.get_by_id(project_id)
        if not project:
            return None
        
        update_data = project_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(project, key, value)
        
        await self.db.flush()
        await self.db.refresh(project)
        return project

    async def delete(self, project_id: uuid.UUID) -> bool:
        """Delete a project"""
        project = await self.get_by_id(project_id)
        if not project:
            return False
        await self.db.delete(project)
        return True
