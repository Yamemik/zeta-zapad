from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

from ..common.database import Base
from ..models.orders_entity import Order


class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0)
    order_id = Column(Integer, ForeignKey(Order.id), unique=True)

    order = relationship("Order", back_populates="cart")
