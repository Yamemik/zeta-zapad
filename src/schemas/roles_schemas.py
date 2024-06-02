from pydantic import ConfigDict, BaseModel, Field


class CreateRoleSchema(BaseModel):
    title: str = Field(...)
    code_name: str = Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "title": "Администратор",
                "code_name": "user or admin or owner",
            }
        },
    )

class RoleSchema(BaseModel):
    id: int = Field(...)
    title: str = Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {

            }
        },
    )
