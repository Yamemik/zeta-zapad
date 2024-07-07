from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from ..models import orders_entity
from ..schemas import orders_schema
from ..services import orders_service
from ..common.database import SessionLocal, engine

orders_entity.Base.metadata.create_all(bind=engine)

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
    response_model=list[orders_schema.OrderSchema],
    summary="Получить заказы",
    status_code=status.HTTP_202_ACCEPTED
)
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    orders = orders_service.get_orders(db, skip=skip, limit=limit)
    return orders


@orders_router.get(
    "/{role_id}",
    response_model=orders_schema.OrderSchema,
    summary="Получить заказ по id",
)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_role = orders_service.get_order_by_id(db, order_id=order_id)
    print(db_role)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_role


@orders_router.post(
    "",
    response_model=orders_schema.OrderSchema,
    summary="Создать заказ",
    status_code=status.HTTP_201_CREATED,
)
def write_order(create_schema: orders_schema.OrderCreateSchema, db: Session = Depends(get_db)):
    db_role = orders_service.create_order(db, schema=create_schema)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Order not create")
    return db_role


@orders_router.delete(
    "{role_id}",
    summary="Удалить заказ",
    status_code=status.HTTP_202_ACCEPTED,
)
def remove_order(role_id: int, db: Session = Depends(get_db)):
    role_to_delete = orders_service.delete_order(db, role_id)
    if role_to_delete is None:
        raise HTTPException(status_code=404, detail="Order not delete")
    return role_to_delete
