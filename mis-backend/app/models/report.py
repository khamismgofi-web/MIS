#Report model (generated summaries)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, Enum, ForeignKey, DateTime, func
from app.core.database import Base
import enum, uuid

class ReportType(str, enum.Enum):
    PARTICIPATION = "Participation"  # who joined which project
    EXHIBITION = "Exhibition"  # which projects entered which show
    FULL_SUMMARY = "Full_summary"  # combined overview

class Report(Base):
    __tablename__ = "report"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    report_type: Mapped[ReportType] = mapped_column(Enum(ReportType), nullable=False)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    exhibition_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey('exhibitions.id'), nullable=True)
    generated_by_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('users.id'), nullable=False)
    generated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    exhibition: Mapped['Exhibition | None'] = relationship(back_populates='reports')
    generated_by: Mapped['User'] = relationship(back_populates='reports')