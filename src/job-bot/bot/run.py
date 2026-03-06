import asyncio
from aiogram import Dispatcher, Bot
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer
from bot.main_router.include_routers import include_all_routers
from utils.config_env import load_bot_token
from services.database.database_code import Database
from services.logs.logging import logger

db = Database()


async def main():
    logger.info("Разработчик бота: https://kwork.ru/user/maket14.")
    logger.info("Проект является коммерческим и создан в рамках заказа.")

    await asyncio.sleep(1)

    logger.info("Подготовка к запуску...")

    await asyncio.sleep(1)

    result = db.create_tables()
    if result:
        logger.debug("База данных подключена успешно")
    else:
        logger.critical("Возникла ошибка при подключении к базе данных!")
        return

    await asyncio.sleep(1)

    dp = Dispatcher()
    include_all_routers(dp=dp)

    bot_token = load_bot_token()
    if bot_token:
        logger.debug("Бот успешно запущен!")
    else:
        logger.critical("Возникла ошибка при запуске бота. Токен не найден.")
        return

    session = AiohttpSession(
        api=TelegramAPIServer.from_base("http://localhost:8081",
                                        is_local=True)
    )

    bot = Bot(token=bot_token, session=session)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
