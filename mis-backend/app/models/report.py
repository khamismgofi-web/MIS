#Report model (generated summaries)
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String,Text,Enum,ForeignKey,DateTime,func
from app.core.database import Base
import enum,uuid

class ReportType(str,enum.Enum):
    PARTICIPATION = "Partucipation" #who joined which project
    EXHIBITION = "Exhibition" #which projects entered which show
    FULL_SUMMARY = "Full_summary" #combined overview

class Report(Base):
    __tableName__ = "report"

id:Mapped[uuid.UUId] = mapped_column(primary_key=True,default=uuid.uuid4)
report_type:Mapped[ReportType] = mapped_column(Enum(ReportType),nullable=False)
tittle:Mapped[str] = mapped_column(String(300),nullable=False)
content:Mapped[str] = mapped_column(Text,nullable=False)
exhibition_id:Mapped[uuid.UUID|None] = mapped_column(ForeignKey('User.id'),nullable=True)
generated_by_id:Mapped[uuid.UUID] = mapped_column(ForeignKey('User.id'),nullable=False)
generated_at:Mapped[DateTime] = mapped_column(DateTime(timezone=True),server_default=func.now())


#Relationship
exhibition:Mapped['Exhibition|None'] = relationship(back_populates='reports')
generated_by:Mapped['User'] = relationship(back_populates='reports')