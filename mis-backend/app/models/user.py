# user model
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String,Boolean,DateTime,Enum,func
from app.core.database import Base
import enum,uuid

class UserRole(str,enum.Enum):
    STUDENT = "student"
    STAFF = "staff"
    ADMIN = "admin"

class User(Base):
    __tableName__ = "users"

    id:             Mapped[uuid.UUID] = mapped_column(primary_key=True,default=uuid.uuid4)
    full_name:      Mapped[str] = mapped_column(String(200),nullable=False)
    email:          Mapped[str] = mapped_column(String(255),nullable=False)
    hashed_password:Mapped[str] = mapped_column(String(255), nullable=False)
    role:           Mapped[UserRole] = mapped_column(Enum(UserRole),default=UserRole.STUDENT)
    department:     Mapped[str[None]] = mapped_column(String(200), nullable=False)
    is_active:      Mapped[bool] = mapped_column(Boolean,default=True)
    created_at:     Mapped[DateTime] = mapped_column(DateTime(timezone=True),server_default=func.now())

    #Relationships
    Participations:Mapped[list['Participations']] = relationship(back_populates="user")
    reports:       Mapped[list['Report']] = relationship(back_populates='generated_by')