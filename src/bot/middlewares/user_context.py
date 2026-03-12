from typing import Any, Awaitable, Callable, Dict, Optional

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message, User as TgUser

from src.services.database.main import Database
from src.services.logs.logger import AppLogger, db_logger

from src.bot.handlers.commands.start import start

class UserContextMiddleware(BaseMiddleware):
    def __init__(self, db: Database, logger: AppLogger = db_logger):
        self._db = db
        self._logger = logger

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        data["db"] = self._db
        tg_user: Optional[TgUser] = data.get("event_from_user")

        if tg_user:
            user = None
            try:
                user = await self._db.users.get_user(tg_user.id)
            except Exception as e:
                self._logger.log_middleware_error(e)

            if isinstance(event, Message) and user is None and event.text != "/start":
                return await start(message=event, db=self._db, user=None)

            data["user"] = user

        return await handler(event, data)
