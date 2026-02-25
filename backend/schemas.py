from pydantic import BaseModel
from datetime import date
from typing import List

class TaskCreate(BaseModel):
    title: str

class TaskResponse(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True


class TaskLogCreate(BaseModel):
    task_id: int
    date: date
    completed: bool