from pydantic import BaseModel
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    is_completed: bool = False

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    is_completed: bool
    created_at: str | datetime