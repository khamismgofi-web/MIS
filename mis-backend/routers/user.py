#User CRUD endpoints
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependencies import get_db, get_current_user
from app.services.user_services import UserService
from app.schemas.user import UserCreate, UserRead
from app.models.user import User
import uuid