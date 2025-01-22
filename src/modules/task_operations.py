from dataclasses import dataclass
from typing import Annotated, List, Dict, Union
from fastapi import Depends
from src.common.models import Task, State

@dataclass
class TasksOperations:
    
    storage: List[Task]
    
    def get_tasks(self) -> List[Task]:
        return self.storage
    
    def get_task(self, id: int) -> Union[Task, None]:
        for task in self.storage:
            if task.id == id:
                return task
        return None
    
    def generate_id(self) -> int:
        if len(self.storage) > 0:
            return self.storage[-1].id + 1
        return 0

    def add_task(self, task: Task) -> Task:
        task.id = self.generate_id()
        self.storage.append(task)
        return task
    
    def update_task(self, id: int, upd_task: Task) -> Union[Task, None]:
        for i, t in enumerate(self.storage):
            if t.id == id:
                upd_task.id = id 
                self.storage[i] = upd_task
                return upd_task
        return None
    
    def delete_task(self, id: int) -> bool:
        for task in self.storage:
            if task.id == id:
                self.storage.remove(task)
                return True
        return False

    def get_task_by_status(self, status: State) -> List[Task]:
        return [task for task in self.storage if task.status == status]
                
def get_tasks_operations() -> TasksOperations:
    return TasksOperations([])

TasksOperationsDep = Annotated[TasksOperations, Depends(get_tasks_operations)]
