from pydantic import BaseModel, Field, ConfigDict


class UserCreate(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid"
    )

    username: str = Field(min_length=3, max_length=256)
    age: int = Field(ge=18, le=130)
    team_id: int | None = Field(None, ge=1)

class UserUpdate(BaseModel):
    username: str | None = Field(None, min_length=3, max_length=256)
    age: int | None = Field(None, ge=18, le=130)
    team_id: int | None = None

class UserResponseSchema(UserCreate):
    id:int






