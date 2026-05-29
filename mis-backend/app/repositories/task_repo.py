from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

from app.models.task import Task
from app.schemas.tasks import TaskCreate, TaskUpdate


class TaskRepository:
    """Database operations for tasks"""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, task_data: TaskCreate) -> Task:
        task = Task(
            title=task_data.title,
            description=task_data.description,
            completed=task_data.completed or False,
            priority=task_data.priority or "medium",
            assigned_to=task_data.assigned_to,
            due_date=task_data.due_date,
        )
        self.db.add(task)
        await self.db.flush()
        await self.db.refresh(task)
        return task

    async def get_by_id(self, task_id: uuid.UUID) -> Task | None:
        result = await self.db.execute(select(Task).where(Task.id == task_id))
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 100) -> list[Task]:
        result = await self.db.execute(select(Task).offset(skip).limit(limit))
        return list(result.scalars().all())

    async def update(self, task_id: uuid.UUID, task_data: TaskUpdate) -> Task | None:
        task = await self.get_by_id(task_id)
        if not task:
            return None

        update_data = task_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(task, key, value)

        await self.db.commit()
        await self.db.refresh(task)
        return task 

    async def delete(self, task_id: uuid.UUID) -> bool:
        task = await self.get_by_id(task_id)
        if not task:
            return False
        await self.db.delete(task)
        return True
