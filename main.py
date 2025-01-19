from settings import get_settings
from telegram.bot import run_bot
from telegram.handlers import r as router
from temp_logic import temp_func

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

    # TODO: удалить реликтовую функцию и файл temp_logic
    # temp_func()


if __name__ == "__main__":
    asyncio.run(main())
