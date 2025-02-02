from telegram import fsm
from telegram.messages import texts, keyboards
from dungeon_generation.pre_generation.general_attributes import generate as get_dungeon
from dungeon_generation.area_generation.area_generator import Dungeon

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
    current_state = await state.get_state()
    if current_state in (fsm.GenerateDungeon.proceed_or_retry, fsm.GenerateDungeon.confirmation):
        await callback.message.answer(
            texts.choose_size.get_text_ru(),
            reply_markup=keyboards.choose_size.get_keyboard("ru"),
        )
        await state.set_state(fsm.GenerateDungeon.choosing_size)


# Provide dungeon description -> Генерация областей, retry or back
@r.callback_query(StateFilter(fsm.GenerateDungeon.choosing_size), F.data.in_(("small", "large")))
async def provide_dungeon_description(callback: types.CallbackQuery, state: FSMContext):
    size = await state.get_value("size")
    if not size:
        await state.update_data(size=callback.data)
        size = callback.data
    dungeon = get_dungeon(size)
    dungeon_description = dungeon[0]
    dungeon_dict = dungeon[1]
    # Store dungeon content for future use
    await state.update_data(dungeon=dungeon_dict)

    await callback.message.answer(
        dungeon_description,
        reply_markup=keyboards.proceed.get_keyboard("ru")
    )
    await state.set_state(fsm.GenerateDungeon.proceed_or_retry)


# Generate areas -> Retry or back
@r.callback_query(fsm.GenerateDungeon.proceed_or_retry, F.data == "proceed")
async def get_areas(callback: types.CallbackQuery, state: FSMContext):
    dungeon_dict = await state.get_value("dungeon")
    dungeon = Dungeon(dungeon_dict)
    areas = dungeon.get_areas()

    # Создать лист
    areas_list = []
    # Проитерировать по словарям, превратив каждую пару k, v в строку, и добавить строку в лист
    for k, v in areas.items():
        areas_list.append(f"Area #{k}:\n {v}")
    
    text = "\n\n".join(areas_list)
    
    await callback.message.answer(
        text,
        reply_markup=keyboards.confirmation.get_keyboard("ru")
    )
    await state.set_state(fsm.GenerateDungeon.confirmation)


# Retry -> Generate dungeon description again
@r.callback_query(fsm.GenerateDungeon.proceed_or_retry, F.data == "retry")
async def get_description_again(callback: types.CallbackQuery, state: FSMContext):
    await provide_dungeon_description(callback, state)
