from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from src.bot.handlers.commands.menu import menu

from src.locales.messages import MESSAGES

from src.services.database.main import Database
from src.services.database.models import User
from src.services.logs.logger import bot_logger

router = Router()


@router.callback_query(F.data.startswith("change_language"))
async def change_language(call: types.CallbackQuery, state: FSMContext, db: Database, user: User):
    msg = None

    try:
        new_lang = call.data.split('_')[-1]
        user.language = new_lang

        await db.users.update_user_language(
            user_id=user.id,
            language=new_lang
        )

        await call.answer(
            text=MESSAGES[new_lang]["change_language"],
            show_alert=True,
        )
        await menu(message=call.message, state=state, user=user)
    except Exception as e:
        bot_logger.log_handler_error("change_language", e)
        msg = await call.message.answer(text=MESSAGES[user.language]["unknown_error"])
    finally:
        messages_to_delete = (await state.get_data()).get("messages_to_delete", set())
        if msg:
            messages_to_delete.add(msg.message_id)
        await state.update_data(messages_to_delete=messages_to_delete)

@router.callback_query(F.data == "current_language")
async def current_language(call: types.CallbackQuery, state: FSMContext,user: User):
    msg = None

    try:
        await call.answer(
            text=MESSAGES[user.language]["current_language"],
            show_alert=True
        )
    except Exception as e:
        bot_logger.log_handler_error("current_language", e)
        msg = await call.message.answer(text=MESSAGES[user.language]["unknown_error"])
    finally:
        messages_to_delete = (await state.get_data()).get("messages_to_delete", set())
        if msg:
            messages_to_delete.add(msg.message_id)
        await state.update_data(messages_to_delete=messages_to_delete)