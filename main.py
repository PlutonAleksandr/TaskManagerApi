from fastapi import FastAPI

from database import sync_engine, Base
from routers import users
from routers import teams
from routers import tasks

app = FastAPI()

app.include_router(teams.router)
app.include_router(users.router)
app.include_router(tasks.router)
