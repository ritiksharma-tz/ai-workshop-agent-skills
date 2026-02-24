# Taskify API

Minimal task manager REST API for the AI Skills workshop.

## Quick Start

```bash
cd examples/taskify-api
uv sync
uv run uvicorn taskify_api.main:app --reload
```

Open [http://localhost:8000/docs](http://localhost:8000/docs) to see the Swagger UI.

## Endpoints

| Method   | Path                  | Description       |
|----------|-----------------------|-------------------|
| `GET`    | `/health`             | Health check      |
| `GET`    | `/api/tasks`          | List all tasks    |
| `GET`    | `/api/tasks/{id}`     | Get a task        |
| `POST`   | `/api/tasks`          | Create a task     |
| `PATCH`  | `/api/tasks/{id}`     | Update a task     |
| `DELETE` | `/api/tasks/{id}`     | Delete a task     |

## Running Tests

```bash
uv run pytest -v
```
