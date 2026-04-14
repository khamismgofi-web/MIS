# project model
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String,Text,Enum,ForeignKey,DateTime,func
from app.core.database import Base
import enum,uuid

class ProjectCategory(str,enum.Enum):
    SOFTWARE = "software"
    HARDWARE = "hardware"
    RESEARCH = "research"
    ROBOTICS = "robotics"
    OTHER    = "other"

class ProjectStatus(str,enum.Enum):
    ACTIVE      = "active"
    SUBMITTED   = "submitted"
    APPROVED    = "approved"
    REJECTED    = "rejected"

class Project(Base):
    __tableName__ = "projects"

    id:         Mapped[uuid.UUID] = mapped_column(primary_key=True,default=uuid.uuid4)
    tittle:     Mapped[String]= mapped_column(String(500),nullable=False)
    description:Mapped[str]= mapped_column(Text,nullable=False)
    category:   Mapped[ProjectCategory] = mapped_column(Enum(ProjectCategory),default=ProjectCategory.OTHER)
    status:     Mapped[ProjectStatus] = mapped_column(Enum(ProjectStatus),default=ProjectStatus.ACTIVE)
    supervisor_id:Mapped[uuid.UUID|None] = mapped_column(ForeignKey("users.id"),nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True),server_default=func.now())
    update_at:  Mapped[DateTime|None] = mapped_column(DateTime(timezone=True),onupdate=func.now())
    
    #RelationShips
    Participations:Mapped[list['Participations']] = relationship(back_populates='project')
    show_entries:  Mapped[list['ShowEntry']] = mapped_column(back_populates='projects')
    supervisor:    Mapped['User|None'] = relationship('User',ForeignKey=[super])