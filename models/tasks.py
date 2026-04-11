from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import Base, intpk, str_256
from models.statuses import TaskStatus


class Tasks(Base):
    __tablename__ = "tasks"


    id: Mapped[intpk]
    title: Mapped[str_256]
    description: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[TaskStatus] = mapped_column(default=TaskStatus.not_issued, nullable=False)

    user_id: Mapped[int] = mapped_column(nullable=True, ForeignKey="users.id")
    team_id: Mapped[int] = mapped_column(nullable=True, ForeignKey="teams.id")


