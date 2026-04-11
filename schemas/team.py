from pydantic import BaseModel, Field, ConfigDict


class TeamSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid"
    )