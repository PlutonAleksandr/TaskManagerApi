from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import Base, intpk, str_256
from models.statuses import TaskStatus


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[intpk]
    title: Mapped[str_256]
    priority: Mapped[int] # через pydantic проверять что в диапозоне от 1 до 10
    description: Mapped[str]
    status: Mapped[TaskStatus] = mapped_column(default=TaskStatus.not_issued, nullable=False)
    deadline: Mapped[datetime] = mapped_column(nullable=False)
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    team_id: Mapped[int | None] = mapped_column(ForeignKey("teams.id"), nullable=True)


