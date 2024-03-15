import json
from decimal import Decimal
from typing import Any

from sqlalchemy import (DateTime, ForeignKey, Numeric, String, Text, func, Boolean,
                        JSON)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Mytable(Base):
    __tablename__ = "mytable"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
