from fastapi import APIRouter,HTTPException
from src.common.models import State, Task
from src.modules.task_operations import TasksOperations, TasksOperationsDep


router = APIRouter(prefix="/tasks")


@router.get("/")
async def get_task(
    task_operations: TasksOperationsDep, 
    TasksOperationsDep, 
    status: State | None = None
    ) -> list[Task]:

    if status: 
        return task_operations.get_task_by_status(status)
    return task_operations.get_tasks()


@router.get("/{id}")
async def get_task_by_id(
    task_operations: TasksOperationsDep, 
    TasksOperationsDep, 
    status: State | None = None
    ) -> list[Task]:

    task: Task = task_operations.get_task(id)
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")
    return task

@router.post("/")
async def add_task(
    task_operations: TasksOperationsDep,
    task: Task):

    return task_operations.add_task(task)


@router.put("/{id}")
async def update_task(
    task_operations: TasksOperationsDep,
    id: int, updated_task: Task):

    task: Task = task_operations.update_task(id, updated_task)     
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")
    return task


@router.delete("/{id}")
async def delete_task(
    task_operations: TasksOperationsDep,
    id: int):

    task_operations.delete_task(id)