from app.storage import TaskStorage

storage = TaskStorage()
storage.add("Изучить Python", "Пройти ООП")
print("Задачи:", [t.title for t in storage.get_all()])