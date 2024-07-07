from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from ..common.database import Base


class Order(Base):
	__tablename__ = "orders"

	id = Column(Integer, primary_key=True)
	created_at = Column(DateTime, default=datetime.now())

	products = Column(Integer)
	user_id = Column(Integer, ForeignKey("users.id"))

	user = relationship("User", back_populates="orders")
	cart = relationship("Cart", uselist=False, back_populates="order")
