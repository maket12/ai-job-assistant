from aiogram import Router
from src.bot.handlers.commands import get_commands_router
from src.bot.handlers.inline_buttons import get_inline_buttons_router

def get_main_router() -> Router:
    router = Router()
    router.include_routers(
        get_commands_router(),
        get_inline_buttons_router()
    )
    return router