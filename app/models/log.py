# app/models.py
from sqlalchemy import Column, Integer, String, JSON, DateTime, Index
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Log(Base):
    __tablename__ = "logs"
    
    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    message = Column(String, nullable=False)
    metrics = Column(JSON, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Índices para mejor rendimiento
    __table_args__ = (
        Index('ix_logs_timestamp', timestamp.desc()),
        Index('ix_logs_type_timestamp', type, timestamp.desc())
    )
