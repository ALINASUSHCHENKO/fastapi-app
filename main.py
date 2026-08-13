from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, status

from app.database import init_db
from app.storage import TaskStorage, TaskNotFoundError
from app.schemas import TaskCreate, TaskUpdate, TaskResponse

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="Todo List API", lifespan=lifespan)
storage = TaskStorage()

@app.get("/")
def read_root():
    return {"message": "Welcome to Todo API! Go to /docs for Swagger UI."}

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

@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_data: TaskUpdate):
    try:
        return storage.update(
            task_id=task_id,
            title=task_data.title,
            description=task_data.description,
            is_completed=task_data.is_completed
        )
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    try:
        storage.delete(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="Task not found")