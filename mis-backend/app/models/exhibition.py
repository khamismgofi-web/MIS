from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String,Enum,Text,Date,DateTime,func
from app.core.database import Base
import enum,uuid

class ExhibitionStatus(str,enum.Enum):
    UPCOMING = "Upcoming"
    ONGOING = "Ongoing"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class Exhibition(Base):
    __tablename__ = "exhibitions"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    venue: Mapped[str | None] = mapped_column(String(300), nullable=True)
    event_date: Mapped[Date] = mapped_column(Date, nullable=False)
    status: Mapped[ExhibitionStatus] = mapped_column(Enum(ExhibitionStatus), default=ExhibitionStatus.UPCOMING)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    entries: Mapped[list['ShowEntry']] = relationship(back_populates='exhibition')
    reports: Mapped[list['Report']] = relationship(back_populates='exhibition')