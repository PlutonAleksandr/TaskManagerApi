from pydantic import BaseModel, Field, ConfigDict

from models.statuses import TaskStatus


class TaskSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid"
    )

    title:str = Field(min_length=3, max_length=256)
    priority: int = Field(ge=1, le=10)
    description:str = Field(max_length=1000)
    status:TaskStatus
    user_id: int #сделат проверку на то что id команды существует
    team_id: int #сделат проверку на то что id команды существует