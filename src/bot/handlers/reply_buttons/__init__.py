from aiogram import Router
from .account import router as account_router
from .account_menu import router as account_menu_router
# from .search import router as menu_router

def get_reply_buttons_router() -> Router:
    router = Router()
    router.include_routers(
        account_router, account_menu_router,
    )
    return router