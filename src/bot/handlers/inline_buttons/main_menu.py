from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from src.bot.keyboard.inline_buttons.buttons import create_account_menu_markup

from src.locales.messages import MESSAGES

from src.services.database.models import User
from src.services.logs.logger import bot_logger

router = Router()


@router.callback_query(F.data == "account")
async def account(call: types.CallbackQuery, state: FSMContext, user: User):
    msg = None

    try:
        msg = await call.message.answer(
            text=MESSAGES[user.language]["account_info"].format(
                id=user.id, name=user.first_name, lang=user.language,
                cv_set=('✅' if user.cv_file_id is not None else '❌'),
                created_at=user.created_at.strftime("%Y-%m-%d")
            ),
            reply_markup=create_account_menu_markup(current_language=user.language)
        )
    except Exception as e:
        bot_logger.log_handler_error("account", e)
        msg = await call.message.answer(text=MESSAGES[user.language]["unknown_error"])
    finally:
        messages_to_delete = (await state.get_data()).get("messages_to_delete", set())
        if msg:
            messages_to_delete.add(msg.message_id)
        await state.update_data(messages_to_delete=messages_to_delete)
