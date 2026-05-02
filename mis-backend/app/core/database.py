# Async SQLAlchemy engine & session factoryfrom sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings

# Async engine — echo=True prints all SQL in debug mode (helpful during dev)
engine = create_async_engine(settings.DATABASE_URL, echo=settings.DEBUG)

# Session factory — expire_on_commit=False keeps objects usable after commit
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

class Base(DeclarativeBase):
    pass  # all models inherit from this