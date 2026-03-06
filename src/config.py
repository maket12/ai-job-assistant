import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

data_env = os.getenv("BASE_DATA_DIR", "./data")
DATA_DIR = Path(data_env).resolve()

MEDIA_DIR = DATA_DIR / os.getenv("MEDIA_DIR", "media")

MEDIA_DIR.mkdir(parents=True, exist_ok=True)

# Media
WELCOME_VIDEO = MEDIA_DIR / "welcome.mp4"

# Bot configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")

DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en")
