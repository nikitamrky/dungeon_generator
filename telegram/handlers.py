from aiogram import Router, types
from aiogram.filters import Command


# Создаем роутер
r = Router()


# Хэндлер на команду /start
@r.message(Command("start"))
async def cmd_test1(message: types.Message):
    await message.reply("Test")
