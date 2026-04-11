from sqlalchemy import ForeignKey

from database import Base, intpk, str_256
from sqlalchemy.orm import Mapped, mapped_column

class Users(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    username: Mapped[str_256]
    command: Mapped[str_256 | None] = mapped_column(ForeignKey="commands.id")
