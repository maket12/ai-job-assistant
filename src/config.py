import os
from pathlib import Path
from dotenv import load_dotenv

from src.utils.exceptions import EnvVarMissingError

load_dotenv()

# --- Data filepaths ---
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / os.getenv("DATA_DIR", "data")

MEDIA_DIR = DATA_DIR / os.getenv("MEDIA_DIR", "media")
LOGS_DIR = DATA_DIR / os.getenv("LOGS_DIR", "logs")

MIGRATIONS_DIR = DATA_DIR / os.getenv("MIGRATIONS_DIR", "migrations")
SQL_DIR = MIGRATIONS_DIR / "sql"

MEDIA_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# --- Database configuration
def load_db_config() -> str:
    """Loads database config from environment's variables and returns connection uri"""
    host = os.getenv("DB_HOST")
    if not host:
        raise EnvVarMissingError("DB_HOST")

    port = os.getenv("DB_PORT", 5432)

    user = os.getenv("DB_USER")
    if not user:
        raise EnvVarMissingError("DB_USER")

    password = os.getenv("DB_PASSWORD")
    if not password:
        raise EnvVarMissingError("DB_PASSWORD")

    db_name = os.getenv("DB_NAME")
    if not db_name:
        raise EnvVarMissingError("DB_NAME")

    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

def load_db_test_config() -> str:
    """Loads test database config from environment's variables and returns connection uri"""
    host = os.getenv("TEST_DB_HOST")
    if not host:
        raise EnvVarMissingError("TEST_DB_HOST")

    port = os.getenv("TEST_DB_PORT")
    if not port:
        raise EnvVarMissingError("TEST_DB_PORT")

    user = os.getenv("TEST_DB_USER")
    if not user:
        raise EnvVarMissingError("TEST_DB_USER")

    password = os.getenv("TEST_DB_PASSWORD")
    if not password:
        raise EnvVarMissingError("TEST_DB_PASSWORD")

    db_name = os.getenv("TEST_DB_NAME")
    if not db_name:
        raise EnvVarMissingError("TEST_DB_NAME")

    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


# --- Media paths ---
WELCOME_VIDEO = MEDIA_DIR / "welcome.mp4"
WELCOME_VIDEO_FID = "BAACAgIAAxkBAAMUabJHwGPAr0xFl7vPUNP3KYAu0WUAAmeLAAIiaJlJsyvuJcpMVTU6BA"

# --- Bot's configuration ---
BOT_TOKEN = os.getenv("BOT_TOKEN")

DEFAULT_LANGUAGE = "en"
