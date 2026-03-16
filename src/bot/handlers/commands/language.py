from aiogram import Router, types
from aiogram.filters import Command

from src.bot.keyboard.inline_buttons.buttons import create_change_language_markup

from src.locales.messages import MESSAGES

from src.services.database.models import User
from src.services.logs.logger import bot_logger

router = Router()


@router.message(Command("language"))
async def language(message: types.Message, user: User):
    try:
        await message.answer(
            text=MESSAGES[user.language]["language"],
            reply_markup=create_change_language_markup(),
        )
    except Exception as e:
        bot_logger.log_handler_error("language", e)
        await message.answer(text=MESSAGES[user.language]["unknown_error"])
