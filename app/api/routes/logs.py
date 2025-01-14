# app/api/routes/logs.py
from fastapi import APIRouter, WebSocket, Depends, HTTPException
from typing import List
from ...domain.models.log import LogCreate, LogInDB
from ...application.services.log_service import LogService
from ..dependencies import get_log_service, get_connection_manager

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    connection_manager = Depends(get_connection_manager)
):
    await connection_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            log = LogCreate(**data)
            await log_service.create_log(log)
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await connection_manager.disconnect(websocket)

@router.post("/", response_model=LogInDB)
async def create_log(
    log: LogCreate,
    log_service: LogService = Depends(get_log_service)
):
    return await log_service.create_log(log)

@router.get("/recent", response_model=List[LogInDB])
async def get_recent_logs(
    limit: int = 100,
    log_service: LogService = Depends(get_log_service)
):
    return await log_service.get_recent_logs(limit)
