from fastapi import FastAPI, HTTPException, status
from app.storage import TaskStorage, TaskNotFoundError
from app.schemas import TaskCreate, TaskResponse

app = FastAPI(title="Todo API")
storage = TaskStorage()

@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(is_completed: bool | None = None):
    return storage.get_all(is_completed=is_completed)

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    try:
        return storage.get_by_id(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    return storage.add(title=task_data.title, description=task_data.description)