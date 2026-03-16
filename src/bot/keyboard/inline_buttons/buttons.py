from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.locales.inline_buttons import INLINE_BUTTONS

from src.config import DEFAULT_LANGUAGE
from src.locales.messages import MESSAGES


def create_change_language_markup(languages: dict = INLINE_BUTTONS, current_language: str = DEFAULT_LANGUAGE) -> InlineKeyboardMarkup:
    markup = InlineKeyboardBuilder()

    for key, val in languages.items():
        if key == current_language:
            btn = InlineKeyboardButton(
                text=f"✅{val['language_btn']}",
                callback_data="current_language",
            )
        else:
            btn = InlineKeyboardButton(
                text=val["language_btn"],
                callback_data=f"change_language_{key}"
            )
        markup.add(btn)

    return markup.as_markup()

def create_edit_cv_markup(current_language: str = DEFAULT_LANGUAGE, cv_set: bool = True) -> InlineKeyboardMarkup:
    delete_btn = None
    if cv_set:
        delete_btn = InlineKeyboardButton(
                text=INLINE_BUTTONS[current_language]["edit_cv"][1],
                callback_data="delete_cv"
        )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=INLINE_BUTTONS[current_language]["edit_cv"][0],
                callback_data="upload_cv"
            )
        ],
        [delete_btn] if delete_btn else []
    ])
    return markup

def create_delete_cv_markup(current_language: str = DEFAULT_LANGUAGE) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=INLINE_BUTTONS[current_language]["delete_cv"][0],
                callback_data="delete_confirm",
            )
        ],
        [
            InlineKeyboardButton(
                text=INLINE_BUTTONS[current_language]["delete_cv"][1],
                callback_data="delete_back",
            )
        ]
    ])
    return markup
