# app/application/services/log_service.py
from typing import List
from ...domain.interfaces.log_repository import LogRepository
from ...domain.models.log import LogBase, LogInDB
from ...infrastructure.websocket.connection_manager import ConnectionManager

class LogService:
    def __init__(self, repository: LogRepository, connection_manager: ConnectionManager):
        self.repository = repository
        self.connection_manager = connection_manager

    async def create_log(self, log: LogBase) -> LogInDB:
        # Guardar log
        saved_log = await self.repository.save(log)
        
        # Broadcast a clientes conectados
        await self.connection_manager.broadcast(saved_log)
        
        return saved_log

    async def get_recent_logs(self, limit: int = 100) -> List[LogInDB]:
        return await self.repository.get_recent(limit)