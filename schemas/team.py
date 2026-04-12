from pydantic import BaseModel, Field, ConfigDict


class TeamCreateSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid"
    )
    team_name:str = Field(max_length=256)

class TeamUpdate(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid"
    )
    team_name: str | None = Field(max_length=256)

class TeamResponseSchema(TeamCreateSchema):
    id:int
