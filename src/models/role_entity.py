from sqlalchemy import Column, Integer, String

from ..common.database import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=True, default="")
