from aiogram import Router, types, F

from src.bot.handlers.commands.language import language
from src.bot.keyboard.reply_buttons.buttons import create_account_menu_markup

from src.locales.messages import MESSAGES
from src.locales.reply_buttons import REPLY_BUTTONS

from src.services.database.models import User
from src.services.logs.logger import bot_logger

router = Router()

ACCOUNT_BUTTONS = [REPLY_BUTTONS[l]["main_menu"][1] for l in REPLY_BUTTONS]


@router.message(F.text.in_(ACCOUNT_BUTTONS))
async def account(message: types.Message, user: User):
    try:
        await message.answer(
            text=MESSAGES[user.language]["account_info"].format(
                id=user.id, name=user.first_name, lang=user.language,
                cv_set=('✅' if user.cv is not None else '❌'),
                created_at=user.created_at.strftime("%Y-%m-%d")
            ),
            reply_markup=create_account_menu_markup(current_language=user.language)
        )
    except Exception as e:
        bot_logger.log_handler_error("account", e)
        await message.answer(text=MESSAGES[user.language]["unknown_error"])
