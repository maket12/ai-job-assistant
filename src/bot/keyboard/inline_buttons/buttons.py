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
        ],
        [
            InlineKeyboardButton(text=texts[2], callback_data="main_menu")
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

    markup.row(InlineKeyboardButton(
        text=INLINE_BUTTONS[current_language]["back_btn"],
        callback_data="language_back"
    ))

    return markup.as_markup()

def create_edit_cv_markup(current_language: str = DEFAULT_LANGUAGE, cv_set: bool = True) -> InlineKeyboardMarkup:
    texts = INLINE_BUTTONS[current_language]["edit_cv"]
    
    delete_btn = None
    if cv_set:
        delete_btn = InlineKeyboardButton(
                text=texts[1],
                callback_data="delete_cv"
        )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=texts[0],
                callback_data="upload_cv"
            )
        ],
        [delete_btn] if delete_btn else [],
        [
            InlineKeyboardButton(
                text=texts[2],
                callback_data="edit_cv_back"
            )
        ]
    ])
    return markup

def create_delete_cv_markup(current_language: str = DEFAULT_LANGUAGE) -> InlineKeyboardMarkup:
    texts = INLINE_BUTTONS[current_language]["delete_cv"]
    
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=texts[0],
                callback_data="delete_confirm",
            )
        ],
        [
            InlineKeyboardButton(
                text=texts[1],
                callback_data="delete_back",
            )
        ]
    ])
    return markup

def create_search_markup(current_language: str = DEFAULT_LANGUAGE) -> InlineKeyboardMarkup:
    texts = INLINE_BUTTONS[current_language]["search_menu"]
    
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=texts[0],
                callback_data="vacancies",
            )
        ],
        [
            InlineKeyboardButton(
                text=texts[1],
                callback_data="change_settings",
            )
        ],
        [
            InlineKeyboardButton(
                text=texts[2],
                callback_data="main_menu",
            )
        ]
    ])
    return markup

def create_vacancies_markup(current_language: str = DEFAULT_LANGUAGE, url: str = "https://hh.ru") -> InlineKeyboardMarkup:
    texts = INLINE_BUTTONS[current_language]["vacancies"]

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=texts[0],
                callback_data="refuse",
            )
        ],
        [
            InlineKeyboardButton(
                text=texts[1],
                callback_data="details",
            )
        ],
        [
            InlineKeyboardButton(
                text=texts[2],
                callback_data="create_cv",
            )
        ],
        [
            InlineKeyboardButton(
                text=texts[3],
                url=url,
            )
        ],
        [
            InlineKeyboardButton(
                text=texts[4],
                callback_data="search_menu"
            )
        ]
    ])
    return markup

def create_vacancies_details_markup(current_language: str = DEFAULT_LANGUAGE, url: str = "https://hh.ru") -> InlineKeyboardMarkup:
    texts = INLINE_BUTTONS[current_language]["vacancies"]

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=texts[0],
                callback_data="refuse",
            )
        ],
        [
            InlineKeyboardButton(
                text=texts[4],
                callback_data="return",
            )
        ],
        [
            InlineKeyboardButton(
                text=texts[2],
                callback_data="create_cv",
            )
        ],
        [
            InlineKeyboardButton(
                text=texts[3],
                url=url,
            )
        ]
    ])
    return markup

def create_vacancies_cv_markup(current_language: str = DEFAULT_LANGUAGE, url: str = "https://hh.ru") -> InlineKeyboardMarkup:
    texts = INLINE_BUTTONS[current_language]["vacancies"]

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=texts[0],
                callback_data="refuse",
            )
        ],
        [
            InlineKeyboardButton(
                text=texts[1],
                callback_data="details",
            )
        ],
        [
            InlineKeyboardButton(
                text=texts[4],
                callback_data="return",
            )
        ],
        [
            InlineKeyboardButton(
                text=texts[3],
                url=url,
            )
        ]
    ])
    return markup