from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from src.bot.handlers.commands.menu import menu
from src.bot.state.state_init import UploadCVState

from src.locales.messages import MESSAGES
from src.locales.reply_buttons import REPLY_BUTTONS

from src.bot.utils.cv_utils import cv_is_correct, get_cv_path, delete_cv

from src.services.database.main import Database
from src.services.database.models import User
from src.services.logs.logger import bot_logger

router = Router()


@router.message(UploadCVState.get_cv)
async def get_cv(message: types.Message, state: FSMContext, db: Database, user: User):
    msg = None

    try:
        if message.text and message.text == REPLY_BUTTONS[user.language]["back_button"]:
            return

        if not message.document or not cv_is_correct(
                filename=message.document.file_name,
                mimetype=message.document.mime_type,
        ):
            msg = await message.answer(
                text=MESSAGES[user.language]["cv_not_file"],
                reply_markup=ReplyKeyboardRemove()
            )
            return

        # Delete previous CV if exists
        if user.cv_path:
            delete_cv(cv_path=user.cv_path)

        # Download new CV
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

        msg = await message.answer(
            text=MESSAGES[user.language]["cv_uploaded"],
            reply_markup=ReplyKeyboardRemove()
        )
    except Exception as e:
        bot_logger.log_handler_error("get_cv", e)
        await message.answer(text=MESSAGES[user.language]["unknown_error"])
    finally:
        await state.clear()

        messages_to_delete = (await state.get_data()).get("messages_to_delete", set())
        messages_to_delete = messages_to_delete.union([message.message_id, msg.message_id] if msg else [message.message_id])
        await state.update_data(messages_to_delete=messages_to_delete)

        await menu(message=message, state=state, user=user)
