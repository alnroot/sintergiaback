# app/domain/interfaces/log_repository.py
from abc import ABC, abstractmethod
from typing import List, Optional
from ..models.log import LogBase, LogInDB

class LogRepository(ABC):
    @abstractmethod
    async def save(self, log: LogBase) -> LogInDB:
        pass
    
    @abstractmethod
    async def get_recent(self, limit: int = 100) -> List[LogInDB]:
        pass