# Rollback test server

Minimal FastAPI application with three endpoints:

- `GET /health` returns `{"status": "ok"}`
- `GET /ping` returns `{"message": "pong"}`
- `POST /echo` returns the received JSON object

Run locally:

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

Interactive API docs are available at `http://localhost:8000/docs`.
