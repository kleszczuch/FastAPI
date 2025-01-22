from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.server.routers import task
from src.server.routers import pomodoro
import logging

app = FastAPI()

# Include routers
app.include_router(task.router)
app.include_router(pomodoro.router)

# Add logging
logging.basicConfig(level=logging.INFO)

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logging.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )