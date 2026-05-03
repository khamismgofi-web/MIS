#Project DB querries
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.models.project import project
from app.schemas.projects import projectCreate
import uuid