from typing import Optional

from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from src.bot.keyboard.inline_buttons.buttons import create_main_menu_markup

from src.locales.messages import MESSAGES
from src.config import DEFAULT_LANGUAGE, WELCOME_VIDEO_FID

from src.services.database.main import Database
from src.services.database.models import User
from src.services.logs.logger import bot_logger

router = Router()


@router.message(CommandStart())
async def start(
        message: types.Message, state: FSMContext,
        db: Database, user: Optional[User]
):
    msg = None
    lang = DEFAULT_LANGUAGE
    try:
        if user is None:
            await db.users.create_user(
                user_id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                language=DEFAULT_LANGUAGE
            )
        else:
            lang = user.language

        msg = await message.answer_animation(
            animation=WELCOME_VIDEO_FID,
            caption=MESSAGES[lang]["welcome"],
            reply_markup=create_main_menu_markup(current_language=lang)
        )
    except Exception as e:
        bot_logger.log_handler_error("start", e)
        msg = await message.answer(text=MESSAGES[lang]["unknown_error"])
    finally:
        await state.update_data(messages_to_delete=[message.message_id, msg.message_id] if msg else [message.message_id])
