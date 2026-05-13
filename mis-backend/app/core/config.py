#Loads .env settings via pydantic settings
from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    APP_NAME: str = "MIS Platform"
    DEBUG: bool = False

    model_config = {"env_file": str(Path(__file__).parent.parent.parent / ".env")}

settings = Settings()