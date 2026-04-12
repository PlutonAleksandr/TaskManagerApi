from fastapi import APIRouter, HTTPException
from schemas.team import TeamCreateSchema, TeamResponseSchema, TeamUpdate
from services.teams import TeamsCRUD

router = APIRouter(prefix="/teams", tags=["Teams"])


@router.post("/", response_model=TeamResponseSchema, summary="Создание команды")
def create_team(team_data: TeamCreateSchema):
    return TeamsCRUD.create_team(team_data)


@router.get("/", response_model=list[TeamResponseSchema], summary="Получить все команды")
def get_all_teams():
    return TeamsCRUD.select_all_teams()


@router.get("/{id}", response_model=TeamResponseSchema, summary="Получить команду по id")
def get_team(id: int):
    team = TeamsCRUD.select_team(id)
    if team is not None:
        return team
    raise HTTPException(status_code=404, detail="Команда не найдена")


@router.patch("/{id}", response_model=TeamResponseSchema, summary="Обновить команду")
def update_team(id: int, new_data: TeamUpdate):
    team = TeamsCRUD.update_team(id, new_data)
    if team is not None:
        return team
    raise HTTPException(status_code=404, detail="Команда не найдена")


@router.delete("/{id}", summary="Удалить команду")
def delete_team(id: int):
    result = TeamsCRUD.delete_team(id)
    if result:
        return {"status": "ok"}
    raise HTTPException(status_code=404, detail="Команда не найдена")