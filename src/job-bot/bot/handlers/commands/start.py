import logging
from aiogram import Router, types
from aiogram.filters import CommandStart
from src.locales.messages import MESSAGES
from src.config import DEFAULT_LANGUAGE, WELCOME_VIDEO

logger = logging.getLogger(__name__)

router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    user_lang = message.from_user.language_code
    lang = user_lang if user_lang else DEFAULT_LANGUAGE
    try:
        await message.answer_animation(
            animation=types.FSInputFile(path=WELCOME_VIDEO),
            caption=MESSAGES[lang]["welcome"],
        )
    except FileNotFoundError:
        logger.error(f"File not found: {WELCOME_VIDEO}")
        await message.answer(text=MESSAGES[lang]["welcome"])
    except Exception as e:
        logger.exception(f"Fail occurred in start handler")
        await message.answer(text=MESSAGES[lang]["unknown_error"])
