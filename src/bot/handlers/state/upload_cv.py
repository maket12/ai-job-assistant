from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from src.bot.handlers.reply_buttons.account import account
from src.bot.state.state_init import UploadCV

from src.locales.messages import MESSAGES
from src.utils.cv_utils import cv_is_correct, get_cv_path, delete_cv

from src.services.database.main import Database
from src.services.database.models import User
from src.services.logs.logger import bot_logger

router = Router()


@router.message(UploadCV.get_cv)
async def get_cv(message: types.Message, state: FSMContext, db: Database, user: User):
    try:
        if not message.document or not cv_is_correct(
                filename=message.document.file_name,
                mimetype=message.document.mime_type,
        ):
            await message.answer(
                text=MESSAGES[user.language]["cv_not_file"],
                reply_markup=ReplyKeyboardRemove()
            )
            return

        cv_path = get_cv_path(user_id=user.id, filename=message.document.file_name)

        await message.bot.download(
            file=message.document.file_id,
            destination=cv_path,
        )

        # Update user
        user.cv_file_id = message.document.file_id
        user.cv_path = str(cv_path)

        await db.users.update_user_cv(
            user_id=user.id,
            cv_path=user.cv_path,
            cv_file_id=user.cv_file_id
        )

        # Delete previous CV
        delete_cv(cv_path=cv_path)

        await message.answer(
            text=MESSAGES[user.language]["cv_uploaded"],
            reply_markup=ReplyKeyboardRemove()
        )
    except Exception as e:
        bot_logger.log_handler_error("get_cv", e)
        await message.answer(text=MESSAGES[user.language]["unknown_error"])
    finally:
        await state.clear()
        await account(message=message, user=user)
