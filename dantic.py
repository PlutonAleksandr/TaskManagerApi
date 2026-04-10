from pydantic import BaseModel, Field, EmailStr, ConfigDict
from fastapi import FastAPI


data = {
    "email": "abx@mail.ru",
    "bio": "i am not",
    "age": 12,
}

class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10)
    age: int = Field(ge=0, le=130)

    model_config = ConfigDict(extra="forbid")

    def __str__(self):
        return f"Shema User {self.email}"

app = FastAPI()
users = []

@app.post("/users")
def add_user(user: UserSchema):
    users.append(user)
    return {"status": "ok"}

@app.get("/users")
def get_all_users() -> list[UserSchema]:
    return users