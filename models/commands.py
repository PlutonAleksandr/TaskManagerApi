from sqlalchemy.orm import Mapped

from database import Base, intpk, str_256


class Commands(Base):
    id: Mapped[intpk]
    command_name: Mapped[str_256]
