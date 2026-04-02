import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration loaded from environment variables."""
    MONGO_URI = os.getenv("MONGO_URI")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    DEBUG = os.getenv("FLASK_DEBUG", "False").lower() in ("true", "1")


# Keep backward compatibility
MONGO_URI = Config.MONGO_URI
GEMINI_API_KEY = Config.GEMINI_API_KEY
SECRET_KEY = Config.SECRET_KEY
