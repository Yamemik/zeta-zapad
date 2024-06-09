from random import randint

from sqlalchemy.orm import Session

from ..services.roles_service import get_role_by_code

from ..models.users_entity import User
from ..schemas.users_schema import UserUpdateSchema, CreateUsersSchema


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def get_user_by_telephone(db: Session, telephone: str) -> User | None:
    return db.query(User).filter(User.telephone == telephone).first()


def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, email: str, telephone: str):
    verification_code = str(randint(1000, 9999))
    role = get_role_by_code(db, "user")

    db_user = User(
        email=email,
        telephone=telephone,
        password=verification_code,
        role_id=role.id,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, schema: UserUpdateSchema):
    user_db = db.query(User).get(schema.id)

    user_db.name = schema.name


    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db


def update_code_user(db: Session, user_id):
    verification_code = str(randint(1000, 9999))

    user_db = db.query(User).get(user_id)

    user_db.password = verification_code

    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db


def create_owner(db: Session, role_id: int, email: str, telephone: str):
    user = db.query(User).filter(User.role_id == role_id).first()
    if user is None:
        verification_code = str(randint(1000, 9999))
        user = User(
            email=email,
            telephone=telephone,
            password=verification_code,
            role_id=role_id
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    return user


def create_users(db: Session, schema: CreateUsersSchema):
    verification_code = str(randint(1000, 9999))
    role = get_role_by_code(db, schema.role_value)

    db_user = User(
        email=schema.email,
        telephone=schema.telephone,
        name=schema.name,
        second_name=schema.second_name,
        password=verification_code,
        role_id=role.id,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
