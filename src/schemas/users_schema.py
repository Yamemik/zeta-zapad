from datetime import datetime
from pydantic import ConfigDict, BaseModel, Field, EmailStr

from ..schemas.carts_schema import CartSchema


class UserCreateSchema(BaseModel):
    email: str = Field()
    telephone: str = Field()

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "email": "kuancarlos@yandex.ru",
                "telephone": "+79993335577"
            }
        },
    )


class UserUpdateSchema(UserCreateSchema):
    name: str = Field(default="")
    second_name: str = Field(default="")

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "Олег",
                "second_name": "Иванов",
            }
        },
    )


class UserSchema(UserUpdateSchema):
    id: int = Field(...)
    created_at: datetime = Field(...)

    # carts: list[CartSchema] = []

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {

            }
        },
    )
