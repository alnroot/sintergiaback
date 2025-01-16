# app/websocket/connection_manager.py
from fastapi import WebSocket
import logging
from typing import Set
import asyncio
import random
from datetime import datetime

logger = logging.getLogger(__name__)

class ConnectionManager:
    def __init__(self):
        self.active_connections: Set[WebSocket] = set()
        self.log_generator_task = None

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.add(websocket)
        if not self.log_generator_task:
            self.log_generator_task = asyncio.create_task(self.generate_logs())
        logger.info(f"Client connected. Total connections: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        logger.info(f"Client disconnected. Total connections: {len(self.active_connections)}")
        if len(self.active_connections) == 0 and self.log_generator_task:
            self.log_generator_task.cancel()
            self.log_generator_task = None

    async def broadcast(self, message: dict):
        disconnected = set()
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception as e:
                logger.error(f"Error sending message: {e}")
                disconnected.add(connection)
        
        for conn in disconnected:
            self.active_connections.remove(conn)

    async def generate_logs(self):
        log_types = ["system", "patterns", "analysis"]
        status_options = ["normal", "warning", "critical"]
        pattern_types = ["Emergence","Information Sharing", "Phase Transitions", "Synchronization", "Cluster Formation", "Collective Efficiency"]
        
        try:
            while True:
                log_type = random.choice(log_types)
                status = random.choice(status_options)
                
                # Personalizar el mensaje según el tipo de log
                if log_type == "patterns":
                    pattern = random.choice(pattern_types)
                    message = f"Pattern {pattern} detected in neural network"
                    metrics = {
                        "confianza": f"{random.uniform(75, 99):.1f}%",
                        "impacto": random.randint(1, 10),
                        "tipo": pattern
                    }
                elif log_type == "analysis":
                    message = f"System analysis {status}: processing neural patterns"
                    metrics = {
                        "estado": status,
                        "carga": f"{random.uniform(20, 95):.1f}%",
                        "eficiencia": f"{random.uniform(80, 99):.1f}%"
                    }
                else:  # system
                    message = f"System health check: {status}"
                    metrics = {
                        "estado": status,
                        "memoria": f"{random.uniform(30, 85):.1f}%",
                        "latencia": f"{random.uniform(10, 100):.0f}ms"
                    }

                log = {
                    "type": log_type,
                    "message": message,
                    "metrics": metrics,
                    "timestamp": datetime.utcnow().isoformat()
                }

                await self.broadcast(log)
                await asyncio.sleep(5)  # Esperar 5 segundos

        except asyncio.CancelledError:
            logger.info("Log generator stopped")
        except Exception as e:
            logger.error(f"Error in log generation: {e}")