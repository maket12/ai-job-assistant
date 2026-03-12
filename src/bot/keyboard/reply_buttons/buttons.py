from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from src.locales.reply_buttons import REPLY_BUTTONS

from src.config import DEFAULT_LANGUAGE

def create_main_menu_markup(lang: str = DEFAULT_LANGUAGE) -> ReplyKeyboardMarkup:
    buttons = []
    for btn_text in REPLY_BUTTONS[lang]["main_menu"]:
        buttons.append([KeyboardButton(text=btn_text)])

    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    return markup
