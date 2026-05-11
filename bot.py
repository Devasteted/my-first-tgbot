# bot.py — точка входа. Запуск: python bot.py

import asyncio
import logging
from os import getenv

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import router

# Читаем BOT_TOKEN из файла .env
load_dotenv()

# Логи — видим все входящие запросы и ошибки в терминале
logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=getenv("BOT_TOKEN"))
    dp  = Dispatcher()

    # Подключаем роутер — все хэндлеры из handlers.py теперь активны
    dp.include_router(router)

    # Сбрасываем старые обновления и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
