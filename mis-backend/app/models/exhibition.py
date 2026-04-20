from sqlalchemy import Mapped,mapped_column,relationship
from sqlalchemy import String,Enum,Text,Date,DateTime,func
from app.core.database import Base
import enum,uuid

class ExhibitionStatus(str,enum.Enum):
    UPCOMING = "Upcoming"
    ONGOING = "Ongoing"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class Exhibition(Base):
    __tableName__ = "Exihibitions"


id: Mapped[uuid.UUId] = mapped_column(primary_key=True,default=uuid.uuid4)
name:Mapped[String] = mapped_column(String(255),nullable=False)
description:Mapped[str|None] = mapped_column(Text,nullable=True)
venue:Mapped[str|None] = mapped_column(String(300))