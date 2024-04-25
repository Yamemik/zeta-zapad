from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from ..common.database import Base


class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0)

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="carts")
