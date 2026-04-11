from pydantic import BaseModel, Field, ConfigDict


class UserCreate(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid"
    )

    username: str = Field(min_length=3, max_length=256)
    age: int = Field(ge=18, le=130)
    team_id: int | None

class UserResponseShema(UserCreate):
    id:int






