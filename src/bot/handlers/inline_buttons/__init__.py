from aiogram import Router
from .main_menu import router as main_menu_router
from .account_menu import router as account_menu_router
from .change_language import router as change_language_router
from .edit_cv import router as edit_cv_router

def get_inline_buttons_router() -> Router:
    router = Router()
    router.include_routers(
        main_menu_router, account_menu_router,
        change_language_router, edit_cv_router
    )
    return router
