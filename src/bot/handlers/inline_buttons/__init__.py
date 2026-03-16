from aiogram import Router
from .change_language import router as change_language_router
from .edit_cv import router as edit_cv_router

def get_inline_buttons_router() -> Router:
    router = Router()
    router.include_routers(
        change_language_router, edit_cv_router
    )
    return router
