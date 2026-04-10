from sqlalchemy.orm import Mapped, mapped_column

from database import Base, intpk, str_256
from models.target import TargetType


class Tasks(Base):
    id: Mapped[intpk]
    title: Mapped[str_256]
    description: Mapped[str] = mapped_column(nullable=False)

    target_type: Mapped[TargetType] = mapped_column(nullable=True)
    target_name: Mapped[str_256]


