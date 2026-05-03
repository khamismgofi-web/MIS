# get_db(),get_current_use() via Depends()from typing import AsyncGenerator
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession,AsyncGenerator
from app.core.database import AsyncSessionLocal
from app.core.security import verify_token
from app.repositories.user_repo import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/auth/login')

# Provides a DB session to every route — commits on success, rolls back on error
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise

# Decodes JWT and returns the authenticated User object
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db:    AsyncSession = Depends(get_db),
):
    payload = verify_token(token)      # raises 401 if token invalid/expired
    user = await UserRepository(db).get_by_id(payload['sub'])
    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail='User not found or inactive')
    return user

# Admin-only dependency — wrap get_current_user with a role check
async def get_admin_user(current_user = Depends(get_current_user)):
    if current_user.role != 'admin':
        raise HTTPException(status_code=403, detail='Admin access required')
    return current_user