from pydantic import ConfigDict, BaseModel, Field


class CreateRoleSchema(BaseModel):
    title: str = Field(...)
    value: str = Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "title": "Администратор или Менеджер или Пользователь",
                "value": "admin or manager or user",
            }
        },
    )


class RoleSchema(BaseModel):
    id: int = Field(...)
    title: str = Field(...)
    value: str = Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {

            }
        },
    )
