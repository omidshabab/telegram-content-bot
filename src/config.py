import os
from dataclasses import dataclass
from dotenv import load_dotenv
from pathlib import Path

# Find the root directory of the project (where .env should be)
root_dir = Path(__file__).parent.parent
env_path = root_dir / '.env'

# Load the environment variables from .env file
load_dotenv(dotenv_path=env_path)

@dataclass
class Config:
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHANNEL_ID: str = os.getenv("TELEGRAM_CHANNEL_ID")
    TELEGRAM_CHANNEL_USERNAME: str = os.getenv("TELEGRAM_CHANNEL_USERNAME")
    CONTENT_TOPICS: str = os.getenv("CONTENT_TOPICS")
    
    def validate(self):
        required_vars = ["GEMINI_API_KEY", "TELEGRAM_BOT_TOKEN", "TELEGRAM_CHANNEL_ID", "TELEGRAM_CHANNEL_USERNAME", "CONTENT_TOPICS"]
        missing_vars = [var for var in required_vars if not getattr(self, var)]
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
            
        print("Environment variables loaded successfully")