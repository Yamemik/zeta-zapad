from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from ..common.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    name = Column(String, nullable=True, default="")
    second_name = Column(String, nullable=True, default="")
    telephone = Column(String, unique=True, index=True)
    role_id = Column(Integer, ForeignKey("roles.id"))
    email = Column(String, index=True)
    password = Column(String)

    role = relationship("Role", back_populates="users")

    orders = relationship("Order", back_populates="user")
    users = relationship("User", back_populates="role")
