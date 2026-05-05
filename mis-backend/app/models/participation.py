# participation (user -> project join table)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, Enum, func, UniqueConstraint
from app.core.database import Base
import enum, uuid

class ParticipationRole(str, enum.Enum):
    LEAD = "Lead"
    MEMBER = "Member"
    OBSERVER = "Observer"

class Participation(Base):
    __tablename__ = "participation"
    __table_args__ = (UniqueConstraint('user_id', 'project_id', name="uq_user_project"),)

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('users.id'), nullable=False)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('projects.id'), nullable=False)
    role: Mapped[ParticipationRole] = mapped_column(Enum(ParticipationRole), default=ParticipationRole.MEMBER)
    join_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    user: Mapped['User'] = relationship(back_populates='participation')
    project: Mapped['Project'] = relationship(back_populates='participation')