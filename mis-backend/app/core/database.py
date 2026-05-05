# Async SQLAlchemy engine & session factory
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass  # all models inherit from this

# Lazy initialization of engine and session factory
_engine = None
_AsyncSessionLocal = None

def get_engine():
    global _engine
    if _engine is None:
        from app.core.config import settings
        _engine = create_async_engine(settings.DATABASE_URL, echo=settings.DEBUG)
    return _engine

def get_async_session_local():
    global _AsyncSessionLocal
    if _AsyncSessionLocal is None:
        _AsyncSessionLocal = async_sessionmaker(
            bind=get_engine(),
            class_=AsyncSession,
            expire_on_commit=False,
        )
    return _AsyncSessionLocal

# For backward compatibility
@property
def engine():
    return get_engine()

@property
def AsyncSessionLocal():
    return get_async_session_local()