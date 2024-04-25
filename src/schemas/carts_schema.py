from pydantic import ConfigDict, BaseModel, Field, EmailStr


class CartCreateSchema(BaseModel):
    user_id: EmailStr = Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "user_id": "user_id",
            }
        },
    )


class CartUpdateSchema(CartCreateSchema):
    products: list = Field(...)
    quantity: int = Field(...)
    price: float = Field(...)

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


class CartSchema(CartUpdateSchema):
    id: int = Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {

            }
        },
    )
