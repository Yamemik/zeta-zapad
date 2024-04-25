from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from ..models import carts_entity
from ..schemas import carts_schema
from ..services import users_service
from ..common.database import SessionLocal, engine

carts_entity.Base.metadata.create_all(bind=engine)

carts_router = APIRouter(
    prefix="/api/carts",
    tags=["Корзины"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


