from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        onupdate=func.now(),
    )

class Route(Base):
    __tablename__ = "route"
    name: Mapped[str] = mapped_column(String(300))
    latitude: Mapped[float] = mapped_column(Float(10))
    longitude: Mapped[float] = mapped_column(Float(10))
    def __repr__(self) -> str:
        return f"Route(id={self.id!r}, name={self.name!r}, latitude={self.latitude!r}, longitude={self.longitude!r})"