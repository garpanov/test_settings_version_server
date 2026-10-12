from typing import Any

from fastapi import FastAPI


app = FastAPI(title="Rollback test server")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/ping")
async def ping() -> dict[str, str]:
    return {"message": "pong"}

@app.get("/pong")
async def pong() -> dict[str, str]:
    return {"message": "ping"}

@app.get("/dog")
async def pong() -> dict[str, str]:
    return {"message": "cat"}

@app.post("/echo")
async def echo(payload: dict[str, Any]) -> dict[str, Any]:
    return payload
