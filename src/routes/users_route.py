from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from ..models import users_entity
from ..schemas import users_schema
from ..services import users_service
from ..common.database import SessionLocal, engine

users_entity.Base.metadata.create_all(bind=engine)

users_router = APIRouter(
    prefix="/api/users",
    tags=["Пользователи"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@users_router.get(
    "",
    response_model=list[users_schema.UserSchema],
    summary="Получить пользователей",
)
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = users_service.get_users(db, skip=skip, limit=limit)
    return users


@users_router.get(
    "/{user_id}",
    response_model=users_schema.UserSchema,
    summary="Получить пользователя по id",
)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = users_service.get_user_by_id(db, user_id=user_id)
    print(db_user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
