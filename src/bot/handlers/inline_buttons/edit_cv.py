from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from src.bot.handlers.reply_buttons.account_menu import edit_cv

from src.bot.keyboard.reply_buttons.buttons import create_back_markup
from src.bot.keyboard.inline_buttons.buttons import create_delete_cv_markup

from src.bot.state.state_init import UploadCV

from src.locales.messages import MESSAGES

from src.services.database.main import Database
from src.services.database.models import User
from src.services.logs.logger import bot_logger

router = Router()


@router.callback_query(F.data == "upload_cv")
async def upload_cv(call: types.CallbackQuery, state: FSMContext, db: Database, user: User):
    try:
        await call.message.delete()
        await call.message.answer(
            text=MESSAGES[user.language]["upload_cv"],
            reply_markup=create_back_markup(current_language=user.language)
        )
        await state.set_state(UploadCV.get_cv)
    except Exception as e:
        bot_logger.log_handler_error("upload_cv", e)
        await call.message.answer(text=MESSAGES[user.language]["unknown_error"])

@router.callback_query(F.data == "delete_cv")
async def delete_cv(call: types.CallbackQuery, user: User):
    try:
        await call.message.answer(
            text=MESSAGES[user.language]["delete_cv"],
            reply_markup=create_delete_cv_markup(current_language=user.language)
        )
    except Exception as e:
        bot_logger.log_handler_error("delete_cv", e)
        await call.message.answer(text=MESSAGES[user.language]["unknown_error"])

@router.callback_query(F.data == "delete_confirm")
async def delete_confirm(call: types.CallbackQuery, db: Database, user: User):
    try:
        await db.users.update_user_cv(user_id=user.id, cv=None)
        await call.message.delete()
        await call.message.answer(text=MESSAGES[user.language]["cv_deleted"])
    except Exception as e:
        bot_logger.log_handler_error("delete_confirm", e)
        await call.message.answer(text=MESSAGES[user.language]["unknown_error"])

@router.callback_query(F.data == "delete_back")
async def delete_back(call: types.CallbackQuery, user: User):
    try:
        await call.message.delete()
        await edit_cv(message=call.message, user=user)
    except Exception as e:
        bot_logger.log_handler_error("delete_confirm", e)
        await call.message.answer(text=MESSAGES[user.language]["unknown_error"])
