from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from ..models import roles_entity
from ..schemas import roles_schemas
from ..services import roles_service
from ..common.database import SessionLocal, engine

roles_entity.Base.metadata.create_all(bind=engine)

orders_router = APIRouter(
    prefix="/api/orders",
    tags=["Заказы пользователей"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@orders_router.get(
    "",
    response_model=list[roles_schemas.RoleSchema],
    summary="Получить заказы",
    status_code=status.HTTP_202_ACCEPTED
)
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    roles = roles_service.get_roles(db, skip=skip, limit=limit)
    return roles


@orders_router.get(
    "/{role_id}",
    response_model=roles_schemas.RoleSchema,
    summary="Получить заказ по id",
)
def read_order(role_id: int, db: Session = Depends(get_db)):
    db_role = roles_service.get_role_by_id(db, role_id=role_id)
    print(db_role)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_role


@orders_router.post(
    "",
    response_model=roles_schemas.RoleSchema,
    summary="Создать заказ",
    status_code=status.HTTP_201_CREATED,
)
def write_order(create_schema: roles_schemas.CreateRoleSchema, db: Session = Depends(get_db)):
    db_role = roles_service.create_role(db, schema=create_schema)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Order not create")
    return db_role


@orders_router.delete(
    "{role_id}",
    summary="Удалить заказ",
    status_code=status.HTTP_202_ACCEPTED,
)
def remove_order(role_id: int, db: Session = Depends(get_db)):
    role_to_delete = roles_service.delete_role(db, role_id)
    if role_to_delete is None:
        raise HTTPException(status_code=404, detail="Order not delete")
    return role_to_delete
