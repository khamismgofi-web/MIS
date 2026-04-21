#Loads .env settings via pydantic settings
from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    DATABASE_URL : str
    SECRET_KEY : str
    ALGORITHM : str="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES : int=60
    APP_NAME:  str="MIS Platform"
    DEBUG: bool=False

    model_config={"env_file":".env"}
Setting=Setting()