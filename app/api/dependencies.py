# app/api/dependencies.py
from fastapi import Depends
from ..domain.interfaces.log_repository import LogRepository
from ...repositories.log_repository import MemoryLogRepository
from ...websocket.connection_manager import ConnectionManager
from ..application.services.log_service import LogService

# Singleton instances
log_repository: LogRepository = MemoryLogRepository()
connection_manager = ConnectionManager()
log_service = LogService(log_repository, connection_manager)

def get_log_service() -> LogService:
    return log_service

def get_connection_manager() -> ConnectionManager:
    return connection_manager