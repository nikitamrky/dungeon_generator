from aiogram import Bot, Dispatcher


def setup_bot(token, router):
    bot = Bot(token)
    dp = Dispatcher()
    dp.include_router(router)
    return bot, dp


async def run_bot(token, router):
    bot, dp = setup_bot(token, router)
    await dp.start_polling(bot)
