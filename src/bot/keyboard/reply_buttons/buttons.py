from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from src.locales.reply_buttons import REPLY_BUTTONS
from src.config import DEFAULT_LANGUAGE


def create_back_markup(current_language: str = DEFAULT_LANGUAGE) -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text=REPLY_BUTTONS[current_language]["back_button"])
        ]
    ], resize_keyboard=True)
    return markup

def create_main_menu_markup(current_language: str = DEFAULT_LANGUAGE) -> ReplyKeyboardMarkup:
    buttons = []
    for btn_text in REPLY_BUTTONS[current_language]["main_menu"]:
        buttons.append([KeyboardButton(text=btn_text)])

    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    return markup

def create_account_menu_markup(current_language: str = DEFAULT_LANGUAGE) -> ReplyKeyboardMarkup:
    buttons = []
    for btn_text in REPLY_BUTTONS[current_language]["account_menu"]:
        buttons.append([KeyboardButton(text=btn_text)])

    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    return markup
