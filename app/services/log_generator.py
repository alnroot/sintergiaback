from datetime import datetime
import asyncio
import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)

class LogGenerator:
    def __init__(self, broadcast_callback):
        self.broadcast_callback = broadcast_callback
        self._running = False
        self._task = None

    async def start(self):
        if not self._running:
            self._running = True
            self._task = asyncio.create_task(self._generate_logs())
            logger.info("Log generator started")

    async def stop(self):
        if self._running:
            self._running = False
            if self._task:
                self._task.cancel()
                try:
                    await self._task
                except asyncio.CancelledError:
                    pass
            logger.info("Log generator stopped")

    async def generate_log(self, type: str, message: str, metrics: Optional[Dict] = None):
        log = {
            "type": type,
            "message": message,
            "metrics": metrics or {},
            "timestamp": datetime.utcnow().isoformat()
        }
        await self.broadcast_callback(log)
        return log

    async def _generate_logs(self):
        try:
            while self._running:
                # Aquí puedes agregar tu lógica de generación de logs
                # Por ejemplo, análisis de patrones, métricas del sistema, etc.
                await self.generate_log(
                    "system", 
                    "System check completed",
                    {"status": "healthy", "memory_usage": "45%"}
                )
                await asyncio.sleep(5)  # Ajusta según necesidades
        except Exception as e:
            logger.error(f"Error in log generation: {e}")
            self._running = False
