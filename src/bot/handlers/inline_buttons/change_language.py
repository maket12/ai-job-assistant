from typing import Optional

from aiogram import Router, types, F

from src.bot.handlers.commands.start import start
from src.bot.handlers.commands.menu import menu

from src.locales.messages import MESSAGES

from src.config import DEFAULT_LANGUAGE

from src.services.database.main import Database
from src.services.database.models import User
from src.services.logs.logger import bot_logger


router = Router()

@router.callback_query(F.data.startswith("change_language_"))
async def change_language(call: types.CallbackQuery, db: Database, user: Optional[User]):
    lang = DEFAULT_LANGUAGE
    try:
        if user is None:
            bot_logger.warning(f"⚠️ WARNING: User {call.from_user.id} is not in database but tried to call method \"change_language\"")
            await start(message=call.message, db=db, user=user)
            return

        lang = call.data.split('_')[-1]

        await db.users.update_user(
            user_id=user.id,
            language=lang
        )

        await call.answer(
            text=MESSAGES[lang]["change_language"],
            show_alert=True,
        )

        await menu(message=call.message, db=db, user=user)
    except Exception as e:
        bot_logger.log_handler_error("change_language", e)
        await call.message.answer(text=MESSAGES[lang]["unknown_error"])
