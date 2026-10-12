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

## Docker Compose

Build and run the service locally:

```bash
docker compose up --build -d
```

The API will be available at `http://localhost:8000`. To use another host
port, set `PORT`, for example `PORT=8080 docker compose up -d`.

To pull and run the published GHCR image without rebuilding it locally:

```bash
docker compose pull
docker compose up --no-build -d
```

## GHCR

The `Publish container` GitHub Actions workflow publishes the image to
`ghcr.io/garpanov/test_settings_version_server` on every push to `main`, on
version tags such as `v1.0.0`, and when started manually.

The workflow creates these tags:

- `latest` for the default branch
- branch name
- semantic version tags for `v*` releases
- `sha-<commit>` for an exact commit

If the package is private, authenticate on the server before pulling it:

```bash
echo "$GHCR_TOKEN" | docker login ghcr.io -u garpanov --password-stdin
```

The token needs the `read:packages` permission.
