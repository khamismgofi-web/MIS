#ShowEntry (project <-> exhibition join table)
from sqlalchemy import Mapped,mapped_column,relationship
from sqlalchemy import DateTime,ForeignKey,Enum,func,UniqueConstraint,Text
from app.core.database import Base
import enum,uuid

class EntryStatus(str,enum.Enum):
    PENDING = "Pending"
    ACCEPTED ="Accepted"
    REJECTED = "Rejected"
    WINNER = "Winner"

class ShowEntry(Base):
    __tableName__ = "showEntries"
    __table_args__ =(UniqueConstraint("project_id","exhibition_id",name="uq_project_exhibition"),)

id: Mapped[uuid.UUID] =mapped_column(primary_key=True,defaul=uuid.uuid4)
project_id:Mapped[uuid.UUID]=mapped_column(ForeignKey('project.id'),nullable=False)
exhibition_id:Mapped[uuid.UUID]=mapped_column(ForeignKey('exhibition.id'),nullable=False)
status: Mapped[EntryStatus] = mapped_column(Enum(EntryStatus),default=EntryStatus.PENDING)
notes:Mapped[str|None]= mapped_column(Text,nullable=True)
submitted_at:Mapped[DateTime]= mapped_column(DateTime(timezone=True),server_default=func.now())


#Relationship
project:Mapped['Project'] = relationship(back_populates='show_entries')
exhibition_at:Mapped['Exhibition'] = relationship(back_populates='entries')