from typing import Annotated

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from ..common.database import SessionLocal, engine
from ..models import users_entity
from ..schemas.users_schema import UserCreateSchema
from ..services.auth_service import authenticate_user, create_token
from ..services.users_service import get_user_by_telephone, get_user_by_email

users_entity.Base.metadata.create_all(bind=engine)

auth_router = APIRouter(
    prefix="/api/auth",
    tags=["Авторизация"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@auth_router.post(
    "/token",
    summary="Регистрация - Авторизация",
    status_code=status.HTTP_202_ACCEPTED,
)
async def login_for_access_token(user: UserCreateSchema, db: Session = Depends(get_db)):
    user_db = authenticate_user(db, user.email, user.telephone)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Ошибка авторизации",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"message": "Код отправлен!"}


@auth_router.post("/verify_code")
def verify_code(email: str | None, telephone: str | None, code: str,  db: Session = Depends(get_db)):
    if email is None:
        user_db = get_user_by_telephone(db, telephone)
    else:
        user_db = get_user_by_email(db, email)

    if not user_db and user_db.password == code:
        token = create_token(user_db.id)
        return {
            "token": token,
            "message": "Авторизация успешна!"
        }
    else:
        raise HTTPException(status_code=400, detail="Неверный код подтверждения")
