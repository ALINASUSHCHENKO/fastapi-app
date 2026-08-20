# Todo List REST API (FastAPI + SQLite)

REST API сервис для управления списком задач с персистентным хранением в SQLite.

---

## Возмоэные требования
* Python 3.10+
* Git

---

## Локальный запуск

### 1. Клонирование репозитория
```bash
git clone <https://github.com/ALINASUSHCHENKO/fastapi-app>
cd fastapi-app
```

### 2. Создание и активация виртуального окружения
``` Windows (PowerShell):

python -m venv .venv
.venv\Scripts\Activate.ps1
```

```Linux / macOS:

bash

python3 -m venv .venv
source .venv/bin/activate
```

### 3. Установка зависимостей
```bash

pip install -r requirements.txt
```
### 4. Запуск сервера
```bash

uvicorn main:app --reload
```
### Сервер будет доступен по адресу: http://127.0.0.1:8000