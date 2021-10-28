import time
from datetime import datetime, timezone

from elasticapm.contrib.starlette import ElasticAPM, make_apm_client
from fastapi import Depends, FastAPI

from app.auth import get_user
from app.auth import router as AuthRouter
from app.crud import router as CrudRouter
from app.db import db_session, engine
from app.models import Base, Todo, User
from app.settings import settings


def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


apm = make_apm_client(service_name=settings.APM_NAME, server_url=settings.APM_SERVER)
app = FastAPI()
app.add_middleware(ElasticAPM, client=apm)
app.include_router(AuthRouter)
app.include_router(CrudRouter)


@app.on_event("startup")
def on_startup():
    while True:
        try:
            init_db()
            print("Tables are reset")
            break
        except:
            print("Database not responding yet")
            time.sleep(5)

    # Seed data
    # create 10 users
    # create a few notes for the first user
    users = []
    for i in range(1, 11):
        name = f"user{i}"
        user = User(name=name, password="pass")
        users.append(user)

    user1 = users[0]
    todos = [
        Todo(user=user1, title="Note 1", content="My first Note"),
        Todo(user=user1, title="Note 2", content="Edit this Note"),
        Todo(
            user=user1,
            title="Note 3",
            content="So many Notes",
        ),
        Todo(user=user1, title="Note 4", content="Reminder: make more Notes"),
    ]
    with db_session() as session:
        session.add_all(users)
        session.add_all(todos)


@app.get("/me", response_model=User, response_model_exclude={"password": ...})
def me(user: User = Depends(get_user)):
    return user


@app.get("/error")
def err():
    return 1 / 0
