from datetime import datetime
from enum import Enum
from typing import List
from datetime import timedelta
from pydantic import BaseModel, Field


class State(str, Enum):
    toDo = "toDo"
    inProgress = "inProgress"
    done = "done"



class Task(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...,min_length=3, max_length=100)
    description: str = Field(default="", max_length=300)
    status: State = Field(default=State.toDo)

class Pomodoro(BaseModel):
    task_id: int = Field()
    start_time: datetime = Field(default=datetime.now())
    end_time: datetime = Field(default=datetime.now() + timedelta(minutes=25))
    completed: bool = Field(default=False)