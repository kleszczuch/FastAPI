from fastapi import FastAPI
from src.server.routers import task
from src.server.routers import pomodoro

app = FastAPI()
app.include_router(task.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}