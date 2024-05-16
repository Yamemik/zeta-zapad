from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from sqlalchemy.orm import Session

from ..services.users_service import (get_user_by_email, get_user_by_telephone, create_user, get_user_by_id,
                                      update_code_user)
from ..services.email_service import send_email

SECRET_KEY = "asf5hjjiqvbkpa56"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 480000

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")


class Token(BaseModel):
    access_token: str
    token_type: str


def authenticate_user(db: Session, email: str, telephone: str):
    if email == "":
        user = get_user_by_telephone(db, telephone)
        if not user:
            user = create_user(db, telephone, telephone)
            # send_sms()
        else:
            update_code_user(db, user.id)
            # send_sms()
    else:
        user = get_user_by_email(db, email)
        if not user:
            user = create_user(db, email, email)
            send_email(user.password, email)
        else:
            update_code_user(db, user.id)
            send_email(user.password, email)
    return user


def verify_code(email: str, telephone: str, code: str, db: Session):
    if email != "":
        user_db = get_user_by_email(db, email)
    else:
        user_db = get_user_by_telephone(db, telephone)

    if user_db and user_db.password == code:
        return create_token(user_db.id)
    else:
        return None


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    if expires_delta is None:
        timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_token(user_id: int):
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user_id}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: int = payload.get("sub")
        if id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_id(id)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
        current_user: Annotated[dict, Depends(get_current_user)]
):
    if current_user["role"] is None:
        raise HTTPException(status_code=400, detail="Не авторизован")
    return current_user
