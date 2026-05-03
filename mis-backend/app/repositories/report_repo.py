#Report generation querriesfrom sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.models.report import report
from app.schemas.report import reportCreate
import uuid