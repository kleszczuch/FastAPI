from dataclasses import dataclass
from typing import Annotated
from fastapi import Depends, HTTPException
from datetime import datetime, timedelta

from src.common.models import Pomodoro
from src.modules.task_operations import TasksOperations, TasksOperationsDep

@dataclass
class PomodoroOperations:
    storage = []
    tasks: TasksOperations

    def create_pomodoro(self, task_id: int):
        for task in self.tasks.get_tasks():
            if task["id"] == task_id:
                if any(session["task_id"] == task_id and not session["completed"] for session in self.pomodoro_sessions):
                    raise HTTPException(status_code=400, detail="Task already has an active timer.")
                
                start_time = datetime.now()
                end_time = start_time + timedelta(minutes=25)
                session = {"task_id": task_id, "start_time": start_time, "end_time": end_time, "completed": False}
                self.pomodoro_sessions.append(session)
                return session
        raise HTTPException(status_code=404, detail="Task with the given ID does not exist.")

    def stop_pomodoro(self, task_id: int):
        for session in self.pomodoro_sessions:
            if session["task_id"] == task_id and not session["completed"]:
                session["end_time"] = datetime.now()
                session["completed"] = True
                return session
        raise HTTPException(status_code=400, detail="No active timer for this task.")

    def get_pomodoro_stats(self):
        stats = {}
        total_time = timedelta()
        
        for session in self.pomodoro_sessions:
            if session["completed"]:
                task_id = session["task_id"]
                session_duration = session["end_time"] - session["start_time"]
                total_time += session_duration
                
                if task_id in stats:
                    stats[task_id]["completed_sessions"] += 1
                    stats[task_id]["total_time"] += session_duration
                else:
                    stats[task_id] = {
                        "completed_sessions": 1,
                        "total_time": session_duration
                    }
        return {"total_time": total_time, "stats": stats}
    
    def get_pomodoro(self) -> list[Pomodoro]:
        self.update_pomodoro()
        return self.storage

def get_pomodoro_operations(tasks_operations: TasksOperations = Depends(TasksOperationsDep)) -> PomodoroOperations:
    return PomodoroOperations(storage=[], tasks=tasks_operations, pomodoro_sessions=[])

PomodoroOperationsDep = Annotated[PomodoroOperations, Depends(get_pomodoro_operations)]