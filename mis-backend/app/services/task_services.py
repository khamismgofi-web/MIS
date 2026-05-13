from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.tasks import TaskCreate, TaskRead, TaskUpdate
from app.repositories.task_repo import TaskRepository
from app.models.user import User


class TaskService:
    """Business logic for task management"""

    def __init__(self, db: AsyncSession):
        self.repo = TaskRepository(db)

    async def create_task(self, task_data: TaskCreate, current_user: User) -> TaskRead:
        task = await self.repo.create(task_data)
        return TaskRead.model_validate(task)

    async def get_task(self, task_id) -> TaskRead:
        task = await self.repo.get_by_id(task_id)
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        return TaskRead.model_validate(task)

    async def get_all_tasks(self, skip: int = 0, limit: int = 100) -> list[TaskRead]:
        tasks = await self.repo.get_all(skip, limit)
        return [TaskRead.model_validate(task) for task in tasks]

    async def update_task(self, task_id, task_data: TaskUpdate, current_user: User) -> TaskRead:
        task = await self.repo.update(task_id, task_data)
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        return TaskRead.model_validate(task)

    async def delete_task(self, task_id, current_user: User) -> dict:
        deleted = await self.repo.delete(task_id)
        if not deleted:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        return {"message": "Task deleted successfully"}
