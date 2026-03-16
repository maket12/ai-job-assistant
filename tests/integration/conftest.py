import pytest
from src.services.database.repositories.user_repository import UserRepository
from src.services.logs.logger import db_logger

@pytest.fixture
async def user_repo(db_pool):
    await db_pool.execute("TRUNCATE TABLE users CASCADE")
    repo = UserRepository(db_pool, db_logger)
    return repo
