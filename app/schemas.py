from datetime import datetime
from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Название задачи (не пустое)",
    )
    description: str | None = None


class TaskUpdate(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Название задачи (не пустое)",
    )
    description: str | None = None
    is_completed: bool = False


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    is_completed: bool
    created_at: datetime