from app.models import Task

class TaskNotFoundError(Exception):
    pass

class TaskStorage:
    def __init__(self):
        self.tasks = {}
        self._current_id = 1

    def add(self, title: str, description: str = None):
        task = Task(self._current_id, title, description)
        self.tasks[self._current_id] = task
        self._current_id += 1
        return task

    def get_all(self, is_completed: bool = None):
        tasks = list(self.tasks.values())
        if is_completed is not None:
            return [t for t in tasks if t.is_completed == is_completed]
        return tasks

    def get_by_id(self, task_id: int):
        if task_id not in self.tasks:
            raise TaskNotFoundError(f"Task with id {task_id} not found")
        return self.tasks[task_id]