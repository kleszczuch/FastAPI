from dataclasses import dataclass
from typing import Annotated
from fastapi import Depends 


@dataclass
class TasksOperations:
    
    storage = []
    
    def get_tasks(self) -> list:
        return self.storage
    
    def get_task(self, id: int) -> dict:
        for task in self.storage:
            if task["id"] == id:
                return task
        return None
    def generate_id(self) -> int:
        if len(self.storage) > 0:
            return self.storage[-1]["id"] + 1
        return 0

    def add_task(self, task: dict) -> dict:
        task["id"] = len(self.storage) + 1
        self.storage.append(task)
        return task
    
    def update_task(self, id: int, upd_task: dict) -> dict:
        for i, t in enumerate(self.storage):
            if t["id"] == id:
                self.storage[i] = upd_task
                return upd_task
        return None
    
    def delete_task(self, id: int) -> dict:
        for task in self.storage:
            if task["id"] == id:
                self.storage.remove(task)
                return True
        return False
                
def get_taks_operations() -> TasksOperations:
    return TasksOperations([])
    
TasksOperationsDep = Annotated[TasksOperations, Depends(get_taks_operations)]