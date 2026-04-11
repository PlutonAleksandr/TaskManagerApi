from sqlalchemy.orm import Mapped

from database import Base, intpk, str_256


class Teams(Base):
    __tablename__ = "teams"

    id: Mapped[intpk]
    command_name: Mapped[str_256]
