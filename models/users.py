from database import Base, intpk, str_256
from sqlalchemy.orm import Mapped, mapped_column

class Users(Base):
    id: Mapped[intpk]
    username: Mapped[str_256]
    command: Mapped[str_256 | None]
