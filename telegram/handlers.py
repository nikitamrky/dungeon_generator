from telegram.messages import texts, keyboards
from dungeon_generation.pre_generation.general_attributes import generate as get_dungeon

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Создаем роутер
r = Router()


# /start: выбрать размер подземелья
@r.message(Command("start"))
async def choose_size(message: types.Message):
    await message.answer(
        texts.choose_size.get_text_ru(),
        reply_markup=keyboards.choose_size.get_keyboard("ru"),
    )


@r.callback_query(F.data.in_(("small", "large")))
async def approve_dungeon(callback: types.CallbackQuery):
    dungeon_description = get_dungeon(callback.data)
    await callback.message.answer(
        dungeon_description,
    )
