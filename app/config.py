from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str = ""  # Opcional, para caché
    ENV: str = "development"
    
    # Configuración de conexión
    DB_POOL_SIZE: int = 5
    DB_MAX_OVERFLOW: int = 10
    DB_POOL_TIMEOUT: int = 30
    DB_POOL_RECYCLE: int = 1800
    
    # Configuración de logs
    LOG_RETENTION_DAYS: int = 30
    MAX_LOGS_PER_REQUEST: int = 1000
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()