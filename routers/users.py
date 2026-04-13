from fastapi import APIRouter, HTTPException
from schemas import UserCreate, UserResponseSchema, UserUpdate
from services.users import UsersCRUD

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponseSchema, summary="Создание пользователя")
def create_user(user_data: UserCreate):
    try:
        return UsersCRUD.create_user(user_data)
    except ValueError as ex:
        raise HTTPException(status_code=400, detail=str(ex))


@router.get("/", response_model=list[UserResponseSchema], summary="Получить всех пользователей")
def get_all_users():
    return UsersCRUD.select_all_users()

@router.get("/{id}", response_model=UserResponseSchema, summary="Получить пользователя по id")
def get_user(id: int):
    user = UsersCRUD.select_user(id)
    if user is not None:
        return user
    raise HTTPException(status_code=404, detail="Пользователь не найден")


@router.patch("/{id}", response_model=UserResponseSchema, summary="Обновить пользователя")
def update_user(id: int, new_data: UserUpdate):
    try:
        user = UsersCRUD.update_user(id, new_data)
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден")

        return user

    except ValueError as ex:
        raise HTTPException(status_code=400, detail=str(ex))

@router.delete("/{id}", summary="Удалить пользователя")
def delete_user(id: int):
    result = UsersCRUD.delete_user(id)
    if result:
        return {"status": "ok"}
    raise HTTPException(status_code=404, detail="Пользователь не найден")