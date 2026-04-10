import uvicorn
from fastapi import FastAPI, HTTPException


app = FastAPI()

structs = [
    {
        "id":1,
        "title": "first"
    },
    {
        "id": 2,
        "title": "second"
    }
]



@app.get(
    "/structs",
    tags=["Структуры"],
    summary="Получение всех структур"
)
def home():
    return structs


@app.get(
    "/structs/{idx}",
    tags=["Структуры"],
    summary="Получение конкретной структуры"
)
def get_struct(idx:int):
    for st in structs:
        if st["id"] == idx:
            return st
    raise HTTPException(status_code=404, detail="структура не найдена")


from pydantic import BaseModel

class NewStruct(BaseModel):
    title: str


@app.post(
    "/structs",
    tags=["Структуры"],
    summary="Добавление структуры"
)
def create_st(new_struct: NewStruct):
    structs.append(
        {
            "id": len(structs)+1,
            "title": new_struct.title
        }
    )
    return {"success": True}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)