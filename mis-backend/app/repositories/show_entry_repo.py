#ShowEntry DB querries
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.models.show_entry import ShowEntry
from app.schemas.show_entry import showEntryCreate
import uuid