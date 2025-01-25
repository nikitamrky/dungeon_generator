from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


def setup_bot(token, router):
    bot = Bot(token)
    dp = Dispatcher(storage=MemoryStorage())  # TODO: Заменить
    dp.include_router(router)
    return bot, dp


async def run_bot(token, router):
    bot, dp = setup_bot(token, router)
    await dp.start_polling(bot)
