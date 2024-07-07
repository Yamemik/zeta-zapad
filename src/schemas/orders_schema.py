from pydantic import ConfigDict, BaseModel, Field


class OrderCreateSchema(BaseModel):
    user_id: int = Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "user_id": "user_id",
            }
        },
    )


class OrdertUpdateSchema(OrderCreateSchema):
    products: list = Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "user_id": "user_id",
            }
        },
    )


class OrderSchema(OrdertUpdateSchema):
    id: int = Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {

            }
        },
    )
