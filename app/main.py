from asyncio import sleep
from fastapi import BackgroundTasks, Depends, FastAPI

from dependencies import get_query_token, get_token_header
# from .internal import admin
from routers import users
from database.connection import conn
# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()


app.include_router(users.router)
# app.include_router(items.router)
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )


def write_log(message: str):
    with open("log.txt", mode="a") as log:
        sleep(10)
        log.write(message)


def get_query(background_tasks: BackgroundTasks, q: str | None = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)
    return q


@app.on_event("startup")
async def startup():
    await conn.connect()


@app.on_event("shutdown")
async def shutdown():
    await conn.disconnect()


@app.post("/send-notification/{email}")
async def send_notification(
    email: str, background_tasks: BackgroundTasks, q: str = Depends(get_query)
):
    message = f"message to {email}\n"
    background_tasks.add_task(write_log, message)
    return {"message": "Message sent"}
