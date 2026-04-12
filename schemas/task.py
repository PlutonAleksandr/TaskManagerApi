from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict, model_validator

from models.statuses import TaskStatus


class TaskCreateSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid"
    )

    title:str = Field(min_length=3, max_length=256)
    priority: int = Field(ge=1, le=10)
    description:str = Field(max_length=1000)
    deadline: datetime
    status:TaskStatus # проверить правда ли может прийти любая строка, а не мой enum
    user_id: int | None = None
    team_id: int | None = None

    @model_validator(mode="after")
    def check_one_assignment(self):
        if self.user_id is not None and self.team_id is not None:
            raise ValueError("Задача не может быть назначена и пользователю и команде одновременно")
        return self



class TaskUpdateSchema(BaseModel):
    title: str | None = Field(None, min_length=3, max_length=256)
    priority: int | None = Field(None, ge=1, le=10)
    description: str | None = Field(None, max_length=1000)
    deadline: datetime | None = None
    status: TaskStatus | None = None
    user_id: int | None = None
    team_id: int | None = None

    @model_validator(mode="after")
    def check_one_assignment(self):
        if self.user_id is not None and self.team_id is not None:
            raise ValueError("Задача не может быть назначена и пользователю и команде одновременно")
        return self


class TaskResponseSchema(TaskCreateSchema):
    id: int
