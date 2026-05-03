#Exhibition CRUD endpoints
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependencies import get_db, get_current_user
from app.services.exhibition_services import ExhibitionService
from app.schemas.exhibition import ExhibitionCreate, ExhibitionRead
from app.models.user import User
import uuid