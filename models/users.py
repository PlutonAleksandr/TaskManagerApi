from sqlalchemy import ForeignKey

from database import Base, intpk, str_256
from sqlalchemy.orm import Mapped, mapped_column

class Users(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    username: Mapped[str_256] = mapped_column(nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    team_id: Mapped[int | None] = mapped_column(ForeignKey("teams.id"))
