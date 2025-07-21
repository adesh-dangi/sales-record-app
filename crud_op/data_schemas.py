from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import func
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Buyers(Base):
    __tablename__ = "buyers"
    # columns for buyers table
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    mobile = Column(String)
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self) -> str:
        return f"Buyers(id={self.id!r}, name={self.name!r}, created_at={self.created_at!r})"

class Battery_Sales(Base):
    __tablename__ = "battery_sales"
    # columns for battey sales table
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    mobile = Column(String)
    created_at = Column(DateTime, default=func.now)
    updated_at = Column(DateTime, default=func.now)
    order_id = Column(Float)  # double precision in SQLite
    price = Column(Float)
    active_sale = Column(Boolean, default=True)

    def __repr__(self) -> str:
        return f"Battery_Sales(id={self.id!r}, name={self.name!r}, created_at={self.created_at!r})"