from sqlalchemy.orm import Session

from ..models.roles_entity import Role
from ..schemas.roles_schemas import CreateRoleSchema


def get_role_by_id(db: Session, role_id: int) -> Role | None:
    return db.query(Role).filter(Role.id == role_id).first()


def get_roles(db: Session, skip: int = 0, limit: int = 10) -> list | None:
    limit = limit if limit > 10 else 10
    return db.query(Role).offset(skip).limit(limit).all()


def create_role(db: Session, schema: CreateRoleSchema):
    db_role = Role(title=schema.title, value=schema.value)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def create_role_owner(db: Session):
    db_role = Role(title="Владелец", value="owner")
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def get_role_by_code(db: Session, value: str):
    db_role = db.query(Role).filter(Role.value == value).first()
    return db_role


def delete_role(db: Session, code_id: int):
    role_to_delete = db.query(Role).filter_by(id=code_id).first()
    if role_to_delete:
        db.delete(role_to_delete)
        db.commit()
        return role_to_delete
    else:
        return None
