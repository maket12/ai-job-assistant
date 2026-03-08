from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Any, Dict, Callable, Awaitable

class LanguageMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any: pass
