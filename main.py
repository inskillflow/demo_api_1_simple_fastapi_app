"""
Mini FastAPI project — full CRUD for a Task manager
-----------------------------------------------------
Endpoints:
  GET    /tasks              — list all tasks (optional filter: ?completed=true/false)
  GET    /tasks/{id}         — get one task by ID
  POST   /tasks              — create a new task
  PUT    /tasks/{id}         — replace a task entirely
  PATCH  /tasks/{id}         — update specific fields only
  DELETE /tasks/{id}         — delete a task

Run:
  uvicorn main:app --reload

Docs:
  http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

app = FastAPI(
    title="Task Manager API",
    description="Mini CRUD API — GET, POST, PUT, PATCH, DELETE",
    version="1.0.0",
)


# ---------------------------------------------------------------------------
# Pydantic models
# ---------------------------------------------------------------------------

class TaskCreate(BaseModel):
    """Fields required to create a task."""
    title: str
    description: str = ""
    completed: bool = False
    priority: str = "medium"   # low | medium | high


class TaskUpdate(BaseModel):
    """All fields optional — used for PATCH (partial update)."""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[str] = None


class Task(BaseModel):
    """Full task object returned by the API."""
    id: int
    title: str
    description: str
    completed: bool
    priority: str
    created_at: str


# ---------------------------------------------------------------------------
# In-memory database (pre-loaded with sample data)
# ---------------------------------------------------------------------------

def _now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

tasks_db: dict[int, dict] = {
    1: {
        "id": 1,
        "title": "Learn FastAPI",
        "description": "Read the official FastAPI documentation",
        "completed": False,
        "priority": "high",
        "created_at": "2026-03-19 08:00:00",
    },
    2: {
        "id": 2,
        "title": "Build a REST API",
        "description": "Create a CRUD API with GET, POST, PUT, DELETE",
        "completed": True,
        "priority": "high",
        "created_at": "2026-03-19 09:00:00",
    },
    3: {
        "id": 3,
        "title": "Write unit tests",
        "description": "Use pytest and FastAPI TestClient",
        "completed": False,
        "priority": "medium",
        "created_at": "2026-03-19 10:00:00",
    },
    4: {
        "id": 4,
        "title": "Deploy to production",
        "description": "Use Docker and a cloud provider",
        "completed": False,
        "priority": "low",
        "created_at": "2026-03-19 11:00:00",
    },
}

next_id = 5  # auto-increment counter


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/", summary="Root — API info")
def root():
    return {
        "message": "Task Manager API is running",
        "docs": "http://127.0.0.1:8000/docs",
        "total_tasks": len(tasks_db),
    }


@app.get("/tasks", response_model=List[Task], summary="Get all tasks")
def get_tasks(completed: Optional[bool] = None, priority: Optional[str] = None):
    """
    Returns all tasks.
    - Filter by status:   GET /tasks?completed=true
    - Filter by priority: GET /tasks?priority=high
    - Combine filters:    GET /tasks?completed=false&priority=high
    """
    tasks = list(tasks_db.values())

    if completed is not None:
        tasks = [t for t in tasks if t["completed"] == completed]

    if priority is not None:
        tasks = [t for t in tasks if t["priority"] == priority]

    return tasks


@app.get("/tasks/{task_id}", response_model=Task, summary="Get one task by ID")
def get_task(task_id: int):
    """Returns a single task. Returns 404 if the task does not exist."""
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=404,
            detail=f"Task with ID {task_id} not found",
        )
    return tasks_db[task_id]


@app.post("/tasks", response_model=Task, status_code=201, summary="Create a new task")
def create_task(task: TaskCreate):
    """
    Creates a new task and returns it with its assigned ID.
    Required field: **title**
    Optional fields: description, completed, priority
    """
    global next_id
    new_task = {
        "id": next_id,
        **task.model_dump(),
        "created_at": _now(),
    }
    tasks_db[next_id] = new_task
    next_id += 1
    return new_task


@app.put("/tasks/{task_id}", response_model=Task, summary="Replace a task entirely (PUT)")
def replace_task(task_id: int, task: TaskCreate):
    """
    Replaces the entire task with the provided data.
    All fields are overwritten — **title** is required.
    Returns 404 if the task does not exist.
    """
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=404,
            detail=f"Task with ID {task_id} not found",
        )
    updated_task = {
        "id": task_id,
        **task.model_dump(),
        "created_at": tasks_db[task_id]["created_at"],
    }
    tasks_db[task_id] = updated_task
    return updated_task


@app.patch("/tasks/{task_id}", response_model=Task, summary="Partially update a task (PATCH)")
def update_task(task_id: int, update: TaskUpdate):
    """
    Updates only the provided fields. Unspecified fields are left unchanged.
    Returns 404 if the task does not exist.

    Example — mark as completed:
    ```json
    { "completed": true }
    ```
    """
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=404,
            detail=f"Task with ID {task_id} not found",
        )
    for field, value in update.model_dump(exclude_none=True).items():
        tasks_db[task_id][field] = value
    return tasks_db[task_id]


@app.delete("/tasks/{task_id}", status_code=204, summary="Delete a task")
def delete_task(task_id: int):
    """
    Deletes a task permanently.
    Returns 204 No Content on success.
    Returns 404 if the task does not exist.
    """
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=404,
            detail=f"Task with ID {task_id} not found",
        )
    del tasks_db[task_id]
