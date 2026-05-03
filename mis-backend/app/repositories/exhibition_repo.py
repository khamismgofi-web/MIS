#Exhibition DB querries
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.models.exhibition import exhibition
from app.schemas.exhibition import exhibitionCreate
import uuid