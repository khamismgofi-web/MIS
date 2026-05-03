#Report generation endpoints
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependencies import get_db, get_current_user
from app.services.report_services import ReportServiceService
from app.schemas.report import ReportCreate, ReportRead
from app.models.user import User
import uuid