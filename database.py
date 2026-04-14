from typing import Annotated

from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column
from sqlalchemy import create_engine, String
from config import settings


str_256 = Annotated[str, 256]
intpk = Annotated[int, mapped_column(primary_key=True)]


sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False,
)
session_factory = sessionmaker(
    sync_engine,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256),
    }