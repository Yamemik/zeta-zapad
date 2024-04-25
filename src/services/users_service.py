from random import randint

from sqlalchemy.orm import Session

from ..models.users_entity import User
from ..schemas import users_schema


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def get_user_by_telephone(db: Session, telephone: str) -> User | None:
    return db.query(User).filter(User.telephone == telephone).first()


def get_user(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, email: str, telephone: str):
    verification_code = str(randint(1000, 9999))

    db_user = User(email=email, telephone=telephone, password=verification_code)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
