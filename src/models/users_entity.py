from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..common.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    name = Column(String, nullable=True)
    second_name = Column(String, nullable=True)
    telephone = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    carts = relationship("Cart", back_populates="user")
