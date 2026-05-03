#user DB Querries
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.models.user import UserRole
from app.schemas.users import UserCreate
import uuid