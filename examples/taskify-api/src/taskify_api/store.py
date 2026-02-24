import uuid
from datetime import datetime, timezone

from taskify_api.models import Task, TaskCreate, TaskUpdate


class TaskStore:
    def __init__(self) -> None:
        self._tasks: list[Task] = []
        self._seed()

    def _seed(self) -> None:
        samples = [
            ("Buy groceries", "Milk, eggs, bread, and coffee"),
            ("Write unit tests", "Cover the auth module with pytest"),
            ("Review pull request", "Check the new payment integration PR"),
        ]
        for title, desc in samples:
            self.create_task(TaskCreate(title=title, description=desc))

    def list_tasks(self) -> list[Task]:
        return list(self._tasks)

    def get_task(self, task_id: str) -> Task | None:
        return next((t for t in self._tasks if t.id == task_id), None)

    def create_task(self, data: TaskCreate) -> Task:
        task = Task(
            id=str(uuid.uuid4()),
            title=data.title,
            description=data.description,
            completed=False,
            created_at=datetime.now(timezone.utc),
        )
        self._tasks.append(task)
        return task

    def update_task(self, task_id: str, data: TaskUpdate) -> Task | None:
        task = self.get_task(task_id)
        if task is None:
            return None

        idx = next(i for i, t in enumerate(self._tasks) if t.id == task_id)
        updated = task.model_copy(
            update={k: v for k, v in data.model_dump().items() if v is not None}
        )
        self._tasks[idx] = updated
        return updated

    def delete_task(self, task_id: str) -> bool:
        task = self.get_task(task_id)
        if task is None:
            return False
        self._tasks = [t for t in self._tasks if t.id != task_id]
        return True


task_store = TaskStore()
