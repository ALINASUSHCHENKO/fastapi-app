from app.database import get_db_connection

class TaskNotFoundError(Exception):
    pass

class TaskStorage:

    def add(self, title: str, description: str = None) -> dict:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tasks (title, description) VALUES (?, ?)",
                (title, description)
            )
            task_id = cursor.lastrowid
            conn.commit()
            return self.get_by_id(task_id)

    def get_all(self, is_completed: bool = None) -> list[dict]:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            if is_completed is None:
                cursor.execute("SELECT * FROM tasks")
            else:
                cursor.execute(
                    "SELECT * FROM tasks WHERE is_completed = ?",
                    (1 if is_completed else 0,)
                )
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def get_by_id(self, task_id: int) -> dict:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
            row = cursor.fetchone()
            if row is None:
                raise TaskNotFoundError(f"Task with id {task_id} not found")
            return dict(row)

    def update(self, task_id: int, title: str, description: str = None, is_completed: bool = False) -> dict:

        self.get_by_id(task_id)
        
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE tasks 
                SET title = ?, description = ?, is_completed = ? 
                WHERE id = ?
                """,
                (title, description, 1 if is_completed else 0, task_id)
            )
            conn.commit()
            return self.get_by_id(task_id)

    def delete(self, task_id: int) -> None:
        self.get_by_id(task_id)
        
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()