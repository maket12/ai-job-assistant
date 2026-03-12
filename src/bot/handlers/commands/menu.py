from typing import Optional

from aiogram import Router, types
from aiogram.filters import Command

from src.bot.handlers.commands.start import start
from src.bot.keyboard.reply_buttons.buttons import create_main_menu_markup

from src.locales.messages import MESSAGES

from src.config import DEFAULT_LANGUAGE

from src.services.database.main import Database
from src.services.database.models import User
from src.services.logs.logger import bot_logger

router = Router()


@router.message(Command("menu"))
async def menu(message: types.Message, db: Database, user: Optional[User]):
    lang = DEFAULT_LANGUAGE
    try:
        if user is None:
            bot_logger.warning(f"⚠️ WARNING: User {message.from_user.id} is not in database but tried to call method \"language\"")
            await start(message=message, db=db, user=user)
            return

        lang = user.language

        await message.answer(
            text=MESSAGES[lang]["menu"],
            reply_markup=create_main_menu_markup(lang=lang)
        )
    except Exception as e:
        bot_logger.log_handler_error("menu", e)
        await message.answer(text=MESSAGES[lang]["unknown_error"])
