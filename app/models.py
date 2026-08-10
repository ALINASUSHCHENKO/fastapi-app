from datetime import datetime

class Task:
    def __init__(self, task_id: int, title: str, description: str = None):
        self.id = task_id
        self.title = title
        self.description = description
        self.is_completed = False
        self.created_at = datetime.now()