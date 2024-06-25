from pydantic import BaseSettings
import logging
from dotenv import load_dotenv
import os

load_dotenv()
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

logger = logging.getLogger(__name__)

class Settings(BaseSettings):
    PROJECT_NAME: str = 'Database - Engenharia da Computação - UPE Poli'
    VERSION: str = '0.1.0'
    
    DATABASE_URL: str = SQLALCHEMY_DATABASE_URI

settings = Settings()