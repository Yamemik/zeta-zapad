from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..common.database import Base


class Role(Base):
    __tablename__: str = "roles"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    value = Column(String, unique=True)

    users = relationship("User", back_populates="role")
