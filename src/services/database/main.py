import asyncpg

from src.services.database.repositories.user_repository import UserRepository
from src.config import load_db_config

class Database:
    def __init__(self, dsn: str = load_db_config()):
        self.dsn = dsn
        self.__pool = None

        # Repositories
        self.users = None

    @property
    def pool(self) -> asyncpg.Pool:
        return self.__pool

    async def connect(self) -> None:
        """Creates connection pool and initializes repositories"""
        self.__pool = await asyncpg.create_pool(dsn=self.dsn, max_size=15)
        self.users = UserRepository(self.__pool)

    async def disconnect(self) -> None:
        """Closes connection pool if it exists"""
        if self.__pool:
            await self.__pool.close()
