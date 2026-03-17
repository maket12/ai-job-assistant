from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.locales.inline_buttons import INLINE_BUTTONS

from src.config import DEFAULT_LANGUAGE


def create_main_menu_markup(current_language: str = DEFAULT_LANGUAGE) -> InlineKeyboardMarkup:
    texts = INLINE_BUTTONS[current_language]["main_menu"]

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=texts[0], callback_data="search")
        ],
        [
            InlineKeyboardButton(text=texts[1], callback_data="account")
        ]
    ])

    return markup

def create_account_menu_markup(current_language: str = DEFAULT_LANGUAGE) -> InlineKeyboardMarkup:
    texts = INLINE_BUTTONS[current_language]["account_menu"]

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=texts[0], callback_data="change_language")
        ],
        [
            InlineKeyboardButton(text=texts[1], callback_data="edit_cv")
        ]
    ])

    return markup

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
