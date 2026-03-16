from aiogram import Router, types, F

from src.bot.handlers.commands.language import language

from src.bot.keyboard.inline_buttons.buttons import create_edit_cv_markup

from src.locales.messages import MESSAGES
from src.locales.reply_buttons import REPLY_BUTTONS

from src.services.database.models import User
from src.services.logs.logger import bot_logger

router = Router()

CHANGE_LANGUAGE_BUTTONS = {REPLY_BUTTONS[l]["account_menu"][0] for l in REPLY_BUTTONS}
EDIT_CV_BUTTONS = {REPLY_BUTTONS[l]["account_menu"][1] for l in REPLY_BUTTONS}


@router.message(F.text.in_(CHANGE_LANGUAGE_BUTTONS))
async def change_language(message: types.Message, user: User):
    try:
        await language(message=message, user=user)
    except Exception as e:
        bot_logger.log_handler_error("change_language", e)
        await message.answer(text=MESSAGES[user.language]["unknown_error"])

@router.message(F.text.in_(EDIT_CV_BUTTONS))
async def edit_cv(message: types.Message, user: User):
    try:
        if user.cv:
            await message.answer_document(
                document=user.cv,
                caption=MESSAGES[user.language]["current_cv"]
            )
        await message.answer(
            text=MESSAGES[user.language]["edit_cv"],
            reply_markup=create_edit_cv_markup(
                current_language=user.language,
                cv_set=bool(user.cv)
            )
        )
    except Exception as e:
        bot_logger.log_handler_error("edit_cv", e)
        await message.answer(text=MESSAGES[user.language]["unknown_error"])
