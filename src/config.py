import os 
from pathlib import Path
from dotenv import load_dotenv 

project_root = Path(__file__).parent.parent 
load_dotenv(project_root / '.env')

class Config:
    # LLM 
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    
    # Telegram Bot
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
    ALLOWED_TELEGRAM_USER_IDS = os.getenv("ALLOWED_TELEGRAM_USER_IDS", "").split(",")
    
    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite+aiosqlite:///{project_root}/data/app.db")
    
    # Paths 
    DATA_DIR = project_root / "data"
    VECTOR_STORE_DIR = DATA_DIR / "vector_store"
    QDRANT_DB_PATH = DATA_DIR / "qdrant_db" 
    CHECKPOINTS_DIR = DATA_DIR / "checkpoints"
    
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    # FastAPI
    FASTAPI_HOST = os.getenv("FASTAPI_HOST", "0.0.0.0")
    FASTAPI_PORT = int(os.getenv("FASTAPI_PORT", "8000"))
    
    @classmethod 
    def validate(cls) -> None:
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not set in environment variables.")
        if not cls.TELEGRAM_BOT_TOKEN:
            raise ValueError("TELEGRAM_BOT_TOKEN is not set in environment variables.")
        

        cls.DATA_DIR.mkdir(parents=True, exist_ok=True)
        cls.QDRANT_DB_PATH.mkdir(parents=True, exist_ok=True)
        cls.VECTOR_STORE_DIR.mkdir(parents=True, exist_ok=True)
        cls.CHECKPOINTS_DIR.mkdir(parents=True, exist_ok=True) 