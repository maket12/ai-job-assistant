from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.locales.inline_buttons import INLINE_BUTTONS

def create_change_language_markup(languages: dict = INLINE_BUTTONS) -> InlineKeyboardMarkup:
    markup = InlineKeyboardBuilder()

    for key, val in languages.items():
        markup.add(InlineKeyboardButton(text=val["language_btn"], callback_data=f"change_language_{key}"))

    return markup.as_markup()
