from pydantic import BaseModel

class RoleInfo(BaseModel):
    """Information about available user roles"""
    name: str
    description: str

class RolesResponse(BaseModel):
    """Response containing all available roles"""
    roles: list[RoleInfo]
