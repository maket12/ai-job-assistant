from typing import Optional

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from src.bot.handlers.commands.menu import menu

from src.locales.messages import MESSAGES
from src.config import DEFAULT_LANGUAGE, WELCOME_VIDEO_FID

from src.services.database.main import Database
from src.services.database.models import User
from src.services.logs.logger import bot_logger

router = Router()


@router.message(F.text)
async def unknown(message: types.Message, state: FSMContext, user: Optional[User]):
    msg = None

    try:
        msg = await message.answer(text=MESSAGES[user.language]["unknown"])
    except Exception as e:
        bot_logger.log_handler_error("unknown", e)
        msg = await message.answer(text=MESSAGES[user.language]["unknown_error"])
    finally:
        messages_to_delete = (await state.get_data()).get("messages_to_delete", set())
        messages_to_delete = messages_to_delete.union(
            [message.message_id, msg.message_id] if msg else [message.message_id])
        await state.update_data(messages_to_delete=messages_to_delete)

        await menu(message=message, state=state, user=user)
