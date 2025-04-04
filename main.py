from settings import get_settings
from telegram.bot import run_bot
from telegram.handlers import r as router

import asyncio
import logging


async def main():
    # Настройка логирования
    logging.basicConfig(level=logging.INFO)

    # Собрать переменные среды и настройки для запуска приложения
    settings = get_settings()
    token = settings.get_token()

    # Запустить приложение
    await run_bot(token, router)


if __name__ == "__main__":
    asyncio.run(main())
