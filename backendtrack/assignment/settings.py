import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Get the absolute directory path of the assignment folder where settings.py lives
BASE_DIR = Path(__file__).resolve().parent

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.join(BASE_DIR, ".env"),  extra="ignore")

    DB_CONNECTION:str
    
    


settings = Settings()