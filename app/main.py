from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from .websocket.connection_manager import ConnectionManager
import logging
import uvicorn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS configuration updated to only allow sintergia.xyz
origins = [
    "https://sintergia.xyz",
    "http://sintergia.xyz",
    # Include www subdomain if needed
    "https://www.sintergia.xyz",
    "http://www.sintergia.xyz"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # Specify only the methods you need
    allow_headers=["*"],
)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # Verify origin before accepting connection
    client_host = websocket.headers.get("origin")
    if client_host not in origins:
        await websocket.close(4003)
        return
        
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "active_connections": len(manager.active_connections)
    }

@app.get("/")
async def root():
    return {
        "message": "WebSocket API Service",
        "status": "running",
        "endpoints": {
            "websocket": "/ws",
            "health": "/health"
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)