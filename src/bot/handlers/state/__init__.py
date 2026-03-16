from aiogram import Router
from .upload_cv import router as upload_cv_router

def get_state_router() -> Router:
    router = Router()
    router.include_routers(
        upload_cv_router,
    )
    return router