from telegram.messages import texts, keyboards

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Создаем роутер
r = Router()


# /start: выбрать размер подземелья
@r.message(Command("start"))
async def cmd_test1(message: types.Message):
    await message.answer(
        texts.choose_size.get_text_ru(),
        reply_markup=keyboards.choose_size.get_keyboard("ru"),
    )


# @r.message()
