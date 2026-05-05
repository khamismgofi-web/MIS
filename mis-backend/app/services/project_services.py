from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.repositories.project_repo import ProjectRepository
from app.schemas.projects import ProjectCreate, ProjectUpdate, ProjectRead
from app.models.user import User
import uuid

class ProjectService:
    """Business logic for project management"""
    def __init__(self, db: AsyncSession):
        self.repo = ProjectRepository(db)

    async def create_project(self, project_data: ProjectCreate, current_user: User) -> ProjectRead:
        """Create a new project"""
        project = await self.repo.create(project_data)
        return ProjectRead.model_validate(project)

    async def get_project(self, project_id: uuid.UUID) -> ProjectRead:
        """Get project by ID"""
        project = await self.repo.get_by_id(project_id)
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found"
            )
        return ProjectRead.model_validate(project)

    async def get_all_projects(self, skip: int = 0, limit: int = 100) -> list[ProjectRead]:
        """Get all projects"""
        projects = await self.repo.get_all(skip, limit)
        return [ProjectRead.model_validate(p) for p in projects]

    async def update_project(
        self, project_id: uuid.UUID, project_data: ProjectUpdate, current_user: User
    ) -> ProjectRead:
        """Update project (supervisor or admin only)"""
        project = await self.repo.get_by_id(project_id)
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found"
            )
        
        # Check authorization
        is_supervisor = project.supervisor_id == current_user.id
        is_admin = current_user.role == "admin"
        if not (is_supervisor or is_admin):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized"
            )
        
        updated = await self.repo.update(project_id, project_data)
        return ProjectRead.model_validate(updated)

    async def delete_project(self, project_id: uuid.UUID, current_user: User) -> dict:
        """Delete project (supervisor or admin only)"""
        project = await self.repo.get_by_id(project_id)
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found"
            )
        
        is_supervisor = project.supervisor_id == current_user.id
        is_admin = current_user.role == "admin"
        if not (is_supervisor or is_admin):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized"
            )
        
        await self.repo.delete(project_id)
        return {"message": "Project deleted successfully"}
