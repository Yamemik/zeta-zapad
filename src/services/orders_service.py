from sqlalchemy.orm import Session

from ..models.orders_entity import Order
from ..schemas.orders_schema import OrderCreateSchema


def get_order_by_id(db: Session, order_id: int) -> Order | None:
    return db.query(Order).filter(Order.id == order_id).first()


def get_orders(db: Session, skip: int = 0, limit: int = 10) -> list | None:
    limit = limit if limit > 10 else 10
    return db.query(Order).offset(skip).limit(limit).all()


def create_order(db: Session, schema: OrderCreateSchema):
    db_entity = Order(user_id=schema.user_id)
    db.add(db_entity)
    db.commit()
    db.refresh(db_entity)
    return db_entity


def delete_order(db: Session, order_id: int):
    order_to_delete = db.query(Order).filter_by(id=order_id).first()
    if order_to_delete:
        db.delete(order_to_delete)
        db.commit()
        return order_to_delete
    else:
        return None
