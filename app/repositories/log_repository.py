# app/repositories/log_repository.py
from sqlalchemy.orm import Session
from sqlalchemy import desc
from ..models import Log
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

class LogRepository:
    def __init__(self, db: Session):
        self.db = db

    async def create(self, log_data: dict) -> Log:
        try:
            log = Log(**log_data)
            self.db.add(log)
            await self.db.commit()
            await self.db.refresh(log)
            return log
        except Exception as e:
            logger.error(f"Error creating log: {e}")
            await self.db.rollback()
            raise

    async def get_recent(self, limit: int = 100) -> list[Log]:
        return (
            self.db.query(Log)
            .order_by(desc(Log.timestamp))
            .limit(limit)
            .all()
        )

    async def cleanup_old_logs(self, days: int = 30):
        cutoff = datetime.utcnow() - timedelta(days=days)
        try:
            await self.db.query(Log).filter(
                Log.timestamp < cutoff
            ).delete()
            await self.db.commit()
        except Exception as e:
            logger.error(f"Error cleaning old logs: {e}")
            await self.db.rollback()
            raise