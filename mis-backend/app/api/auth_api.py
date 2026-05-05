from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependencies import get_db
from app.services.user_services import UserService
from app.schemas.users import UserCreate, UserRead
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])

class LoginRequest(BaseModel):
    """Login credentials"""
    email: str
    password: str

class TokenResponse(BaseModel):
    """JWT Token response"""
    access_token: str
    token_type: str = "bearer"

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    """Register a new user"""
    return await UserService(db).create_user(user_data)

@router.post("/login", response_model=TokenResponse)
async def login(
    credentials: LoginRequest,
    db: AsyncSession = Depends(get_db),
):
    """Login user and return JWT token"""
    # TODO: Implement JWT token generation
    user_service = UserService(db)
    user = await user_service.repo.get_by_email(credentials.email)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    # TODO: Verify password hash
    # For now, placeholder implementation
    return TokenResponse(
        access_token="token_placeholder",
        token_type="bearer"
    )

@router.post("/logout")
async def logout():
    """Logout user (invalidate token)"""
    # TODO: Implement token blacklist
    return {"message": "Logged out successfully"}

@router.post("/refresh")
async def refresh_token():
    """Refresh JWT token"""
    # TODO: Implement token refresh logic
    return TokenResponse(
        access_token="new_token_placeholder",
        token_type="bearer"
    )
