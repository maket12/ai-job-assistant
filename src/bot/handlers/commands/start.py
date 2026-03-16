from typing import Optional

from aiogram import Router, types
from aiogram.filters import CommandStart

from src.locales.messages import MESSAGES
from src.config import DEFAULT_LANGUAGE, WELCOME_VIDEO_FID

from src.services.database.main import Database
from src.services.database.models import User

from src.services.logs.logger import bot_logger

router = Router()


@router.message(CommandStart())
async def start(message: types.Message, db: Database, user: Optional[User]):
    lang = DEFAULT_LANGUAGE
    try:
        if user is None:
            await db.users.create_user(
                user_id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                language=DEFAULT_LANGUAGE
            )
        else:
            lang = user.language

        await message.answer_animation(
            animation=WELCOME_VIDEO_FID,
            caption=MESSAGES[lang]["welcome"],
        )
    # except FileNotFoundError:
    #     bot_logger.error(f"File not found: {WELCOME_VIDEO}")
    #     await message.answer(text=MESSAGES[lang]["welcome"])
    except Exception as e:
        bot_logger.log_handler_error("start", e)
        await message.answer(text=MESSAGES[lang]["unknown_error"])
