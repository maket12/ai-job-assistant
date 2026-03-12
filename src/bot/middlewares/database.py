from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User as TgUser
from src.services.database.main import Database

class DbMiddleware(BaseMiddleware):
    def __init__(self, db: Database):
        self.db = db

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        data["db"] = self.db

        tg_user: TgUser = data.get("event_from_user")
        if tg_user:
            user = await self.db.users.get_user(tg_user.id)
            data["user"] = user

        return await handler(event, data)
