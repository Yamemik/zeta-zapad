from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from ..common.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    name = Column(String, nullable=True, default="")
    telephone = Column(String, unique=True, index=True)
    cart_id = Column(Integer, ForeignKey("carts.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    cart = relationship("Cart", back_populates="cart")

    user = relationship("User", back_populates="user")
