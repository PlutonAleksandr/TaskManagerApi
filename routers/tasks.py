
from fastapi import APIRouter, HTTPException

from models.statuses import TaskStatus
from schemas import TaskCreateSchema, TaskUpdateSchema, TaskResponseSchema
from schemas.task import TasksListIdsSchema, TasksBulkUpdateSchema
from services import TasksCRUD
from datetime import datetime

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskResponseSchema, summary="Создание задачи")
def create_task(task_data: TaskCreateSchema):
    try:
        return TasksCRUD.create_task(task_data)
    except ValueError as ex:
        raise HTTPException(status_code=400, detail=str(ex))

@router.post("/by-ids", response_model=list[TaskResponseSchema], summary="Получить задачи по списку id")
def get_tasks_by_id(list_id: TasksListIdsSchema):
    return TasksCRUD.select_tasks_by_id(list_id.ids)

@router.get("/statistics", summary="Статистика задач по пользователю или команде")
def get_statistics_by_status(user_id: int | None = None, team_id: int | None = None):
    try:
        stats = TasksCRUD.get_statistics_by_status(user_id, team_id)
        return {"stats": stats}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{id}", response_model=TaskResponseSchema, summary="Получить задачу по id")
def get_task_by_id(id: int):
    task = TasksCRUD.select_task_by_id(id)
    if task is not None:
        return task
    raise HTTPException(status_code=404, detail="Задача не найдена")


@router.get("/", response_model=list[TaskResponseSchema], summary="Получить задачи по фильтрам")
def get_tasks(
        status: TaskStatus | None = None,
        priority: int | None = None,
        deadline: datetime | None = None
):
    return TasksCRUD.get_tasks_with_filters(status, priority, deadline)

@router.patch("/bulk-status", summary="Массовое обновление статусов задач")
def update_tasks_by_status(data: TasksBulkUpdateSchema):
    return {"updated": TasksCRUD.update_tasks_by_status(data.ids, data.status)}


@router.patch("/{id}", response_model=TaskResponseSchema, summary="Обновить задачу")
def update_task(id: int, new_data: TaskUpdateSchema):
    try:
        task = TasksCRUD.update_task(id, new_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if task is not None:
        return task
    raise HTTPException(status_code=404, detail="Задача не найдена")


@router.patch("/{id}/assign", response_model=TaskResponseSchema, summary="Назначить задачу пользователю или команде")
def assign_task(id: int, user_id: int | None = None, team_id: int | None = None):
    try:
        task = TasksCRUD.assign_task(id, user_id, team_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if task is not None:
        return task
    raise HTTPException(status_code=404, detail="Задача не найдена")


@router.delete("/{id}", summary="Удалить задачу")
def delete_task(id: int):
    result = TasksCRUD.delete_task(id)
    if result:
        return {"status": "ok"}
    raise HTTPException(status_code=404, detail="Задача не найдена")


