# participation (user -> project join table)
from sqlalchemy import Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey,DateTime,Enum,func,UniqueConstraint
from app.core.database import Base
import enum,uuid

class ParticipationRole(str,enum,Enum):
    LEAD = "Lead"
    MEMBER = "Member"
    OBSERVER = "Observer"

class Participation(Base):
    __tableName__ = "Participation"
    __table_agre__ = (UniqueConstraint('user_id','project_id',name = "uq_user_ptoject"),)


id : Mapped[uuid.UUID] = mapped_column(primary_key= True,default =uuid.uuid4)
user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('user.id'),nullable = False)
role: Mapped[ParticipationRole] = mapped_column(Enum(ParticipationRole),default = ParticipationRole.MEMBER)
join_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True),server_default=func.now())


#Relationship
User:Mapped['User'] = relationship(back_populates = 'participation')
project:Mapped['Project'] = relationship(back_populates='participation')