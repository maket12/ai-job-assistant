from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.bot.keyboard.inline_buttons.buttons import create_main_menu_markup

from src.locales.messages import MESSAGES

from src.services.database.models import User
from src.services.logs.logger import bot_logger

router = Router()


@router.message(Command("menu"))
async def menu(message: types.Message, state: FSMContext, user: User):
    msg = None
    try:
        msg = await message.answer(
            text=MESSAGES[user.language]["menu"],
            reply_markup=create_main_menu_markup(current_language=user.language)
        )
    except Exception as e:
        bot_logger.log_handler_error("menu", e)
        msg = await message.answer(text=MESSAGES[user.language]["unknown_error"])
    finally:
        await state.update_data(messages_to_delete=[message.message_id, msg.message_id] if msg else [message.message_id])
