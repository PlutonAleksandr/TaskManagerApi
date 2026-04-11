from typing import Annotated

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase, mapped_column
from sqlalchemy import URL, create_engine, text, String, Integer
from config import settings


str_256 = Annotated[str, 256]
intpk = Annotated[int, mapped_column(primary_key=True)]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256),
    }