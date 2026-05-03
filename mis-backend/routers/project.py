#Project CRUD endpointsfrom fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependencies import get_db, get_current_user
from app.services.project_services import ProjectService
from app.schemas.projects import ProjectCreate, ProjectRead
from app.models.user import User
import uuid