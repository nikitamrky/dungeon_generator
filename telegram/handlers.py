from telegram import fsm
from telegram.messages import texts, keyboards
from dungeon_generation.pre_generation.general_attributes import generate as get_dungeon

from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.methods import SendMessage


# Создаем роутер
r = Router()


# /start -> выбрать размер подземелья
@r.message(Command("start"))
async def choose_language(message: types.Message, state: FSMContext):
    await message.answer(
        texts.choose_language.get_text_eng(),
        reply_markup=keyboards.choose_language.get_keyboard()
    )
    await state.set_state(fsm.MainMenu.choosing_language)


@r.callback_query(F.data.in_(("english", "russian")))
async def choose_size(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(language=callback.data)
    # TODO: кэшировать выбранный язык
    await callback.message.answer(
        texts.choose_size.get_text_ru(),
        reply_markup=keyboards.choose_size.get_keyboard("ru"),
    )
    await state.set_state(fsm.GenerateDungeon.choosing_size)


# Back button -> previous state
@r.callback_query(F.data == "back")
async def back_button(callback: types.CallbackQuery, state: FSMContext):
    if state.get_state() == fsm.GenerateDungeon.proceed_or_retry:
        await callback.message.answer(
            texts.choose_size.get_text_ru(),
            reply_markup=keyboards.choose_size.get_keyboard("ru"),
        )
        await state.set_state(fsm.GenerateDungeon.choosing_size)


# Размер подземелья -> Генерация областей, retry or back
@r.callback_query(StateFilter(fsm.GenerateDungeon.choosing_size), F.data.in_(("small", "large")))
async def provide_dungeon_description(callback: types.CallbackQuery, state: FSMContext):
    size = await state.get_value("size")
    if not size:
        await state.update_data(size=callback.data)
        size = callback.data
    dungeon_description = get_dungeon(size)
    await callback.message.answer(
        dungeon_description,
        reply_markup=keyboards.proceed.get_keyboard("ru")
    )
    await state.set_state(fsm.GenerateDungeon.proceed_or_retry)


# Generate areas -> Retry or back
@r.callback_query(fsm.GenerateDungeon.proceed_or_retry, F.data == "proceed")
async def get_areas(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "Пу-пу-пу, тут будет результат генерации областей",
        reply_markup=keyboards.confirmation.get_keyboard("ru")
    )
    await state.set_state(fsm.GenerateDungeon.confirmation)


# Retry -> Generate dungeon description again
@r.callback_query(fsm.GenerateDungeon.proceed_or_retry, F.data == "retry")
async def get_description_again(callback: types.CallbackQuery, state: FSMContext):
    await provide_dungeon_description(callback, state)
