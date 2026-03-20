from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.bot.keyboard.inline_buttons.buttons import create_vacancies_markup

from src.locales.messages import MESSAGES

from src.services.database.models import User
from src.services.logs.logger import bot_logger

router = Router()


@router.message(Command("vacancies"))
async def vacancies(message: types.Message, state: FSMContext, user: User):
    msg = None
    try:
        if user is None:
            await message.answer(text=MESSAGES[user.language]["unknown_user"])
        msg = await message.answer(
            text=MESSAGES[user.language]["search_info"],
            reply_markup=create_vacancies_markup(current_language=user.language)
        )
    except Exception as e:
        bot_logger.log_handler_error("vacancies", e)
        msg = await message.answer(text=MESSAGES[user.language]["unknown_error"])
    finally:
        messages_to_delete = (await state.get_data()).get("messages_to_delete", set())
        messages_to_delete = messages_to_delete.union([message.message_id, msg.message_id] if msg else [message.message_id])
        await state.update_data(messages_to_delete=messages_to_delete)