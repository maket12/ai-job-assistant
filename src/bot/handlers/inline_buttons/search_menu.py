from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from src.bot.handlers.commands.language import language
from src.bot.keyboard.inline_buttons.buttons import (
    create_vacancies_markup,
    create_vacancies_details_markup,
)

from src.locales.messages import MESSAGES

from src.services.database.main import Database
from src.services.database.models import User
from src.services.logs.logger import bot_logger

router = Router()


@router.callback_query(F.data == "vacancies")
async def refuse_vacancy(call: types.CallbackQuery, state: FSMContext, user: User):
    msg = None

    try:
        msg = await call.message.answer(
            text=MESSAGES[user.language]["search_info"],
            reply_markup=create_vacancies_markup(current_language=user.language)
        )
    except Exception as e:
        bot_logger.log_handler_error("vacancies", e)
        msg = await call.message.answer(
            text=MESSAGES[user.language]["unknown_error"]
        )
    finally:
        messages_to_delete = (await state.get_data()).get("messages_to_delete", set())
        messages_to_delete = messages_to_delete.union(
            [call.message.message_id, msg.message_id] if msg else [call.message.message_id])
        await state.update_data(messages_to_delete=messages_to_delete)


@router.callback_query(F.data == "change_settings")
async def vacancy_details(call: types.CallbackQuery, state: FSMContext, user: User):
    msg = None

    try:
        msg = await call.message.answer(
            text=MESSAGES[user.language]["search_details"],
            reply_markup=create_vacancies_details_markup(current_language=user.language)
        )
    except Exception as e:
        bot_logger.log_handler_error("change_settings", e)
        msg = await call.message.answer(
            text=MESSAGES[user.language]["unknown_error"]
        )
    finally:
        messages_to_delete = (await state.get_data()).get("messages_to_delete", set())
        if msg:
            messages_to_delete = messages_to_delete.union([msg.message_id])
        await state.update_data(messages_to_delete=messages_to_delete)
