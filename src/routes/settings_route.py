from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session

from ..schemas import users_schema
from ..services import roles_service, users_service
from ..common.database import SessionLocal, engine
from ..common.settings import settings

# _entity.Base.metadata.create_all(bind=engine)

settings_router = APIRouter(
    prefix="/api/settings",
    tags=["Настройки"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@settings_router.post(
    "",
    response_model=users_schema.UserSchema,
    summary="Создать владельца",
    status_code=status.HTTP_201_CREATED
)
def write_owner(db: Session = Depends(get_db)):
    role = roles_service.get_role_by_code(db, code_name="owner")
    if role is None:
        db_role = roles_service.create_role_owner(db)
        owner = users_service.create_owner(db,
                                           role_id=db_role.id,
                                           email=settings.email,
                                           telephone=settings.telephone)
    else:
        owner = users_service.create_owner(db,
                                           role_id=role.id,
                                           email=settings.email,
                                           telephone=settings.telephone)
    return owner
