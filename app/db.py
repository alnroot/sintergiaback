# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import get_settings
import contextlib

settings = get_settings()

# Configuración específica para Neon
engine = create_engine(
    settings.DATABASE_URL,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=settings.DB_MAX_OVERFLOW,
    pool_timeout=settings.DB_POOL_TIMEOUT,
    pool_recycle=settings.DB_POOL_RECYCLE,
    pool_pre_ping=True,  # Verifica conexión antes de usar
    connect_args={
        "sslmode": "require",  # Requerido para Neon
        "application_name": "tu-app-name"  # Para identificar conexiones
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextlib.contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()