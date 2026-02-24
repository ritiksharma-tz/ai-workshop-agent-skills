import uvicorn
from fastapi import FastAPI, HTTPException

from taskify_api.models import Task, TaskCreate, TaskUpdate
from taskify_api.store import task_store

app = FastAPI(title="Taskify API", version="0.1.0")


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.get("/api/tasks")
def list_tasks() -> list[Task]:
    return task_store.list_tasks()


@app.get("/api/tasks/{task_id}")
def get_task(task_id: str) -> Task:
    task = task_store.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.post("/api/tasks", status_code=201)
def create_task(data: TaskCreate) -> Task:
    return task_store.create_task(data)


@app.patch("/api/tasks/{task_id}")
def update_task(task_id: str, data: TaskUpdate) -> Task:
    task = task_store.update_task(task_id, data)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/api/tasks/{task_id}", status_code=204)
def delete_task(task_id: str) -> None:
    if not task_store.delete_task(task_id):
        raise HTTPException(status_code=404, detail="Task not found")


def run() -> None:
    uvicorn.run("taskify_api.main:app", host="0.0.0.0", port=8000, reload=True)
