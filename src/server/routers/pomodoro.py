from fastapi import APIRouter, HTTPException, Depends
from src.common.models import Pomodoro
from src.modules.pomodoro_operations import PomodoroOperations, PomodoroOperationsDep

router = APIRouter(prefix="/pomodoro")

@router.post("/{task_id}/start")
async def start_pomodoro(
    task_id: int,
    pomodoro_operations: PomodoroOperations = Depends(PomodoroOperationsDep)
    ) -> Pomodoro:

    return pomodoro_operations.create_pomodoro(task_id)

@router.post("/{task_id}/stop")
async def stop_pomodoro(
    task_id: int,
    pomodoro_operations: PomodoroOperations = Depends(PomodoroOperationsDep)
    ) -> Pomodoro:

    return pomodoro_operations.stop_pomodoro(task_id)

@router.get("/stats")
async def get_pomodoro_stats(
    pomodoro_operations: PomodoroOperations = Depends(PomodoroOperationsDep)
    ) -> dict:

    return pomodoro_operations.get_pomodoro_stats()

@router.get("/")
async def get_pomodoro(
    pomodoro_operations: PomodoroOperations = Depends(PomodoroOperationsDep)
    ) -> list[Pomodoro]:

    return pomodoro_operations.get_pomodoro()