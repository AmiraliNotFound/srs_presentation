"""FastAPI + WebSocket Companion Server for Live SRS Quiz & Presentation Sync."""
from fastapi import FastAPI

app = FastAPI(title="SRS Presentation Companion API")

@app.get("/health")
async def health_check():
    return {"status": "ok"}
