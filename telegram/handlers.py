from telegram import fsm
from telegram.messages import texts, keyboards
from dungeon_generation.pre_generation.general_attributes import generate as get_dungeon
from dungeon_generation.pre_generation.pre_generation import Creature
from dungeon_generation.area_generation.area_generator import Dungeon
from helpers import content_to_str, localize_area_header

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
        texts.choose_language.get_text(),
        reply_markup=keyboards.choose_language.get_keyboard()
    )
    await state.set_state(fsm.MainMenu.choosing_language)


@r.callback_query(F.data.in_(("eng", "ru")))
async def choose_size(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(language=callback.data)
    await callback.message.answer(
        texts.choose_size.get_text(callback.data),
        reply_markup=keyboards.choose_size.get_keyboard(callback.data),
    )
    await state.set_state(fsm.GenerateDungeon.choosing_size)


# Back button -> Choose size
@r.callback_query(F.data == "back")
async def back_button(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state in (fsm.GenerateDungeon.proceed_or_retry, fsm.GenerateDungeon.confirmation):
        language = await state.get_value("language")
        await callback.message.answer(
            texts.choose_size.get_text(language),
            reply_markup=keyboards.choose_size.get_keyboard(language),
        )
        await state.set_state(fsm.GenerateDungeon.choosing_size)


# Provide dungeon description -> Генерация областей, retry or back
@r.callback_query(StateFilter(fsm.GenerateDungeon.choosing_size), F.data.in_(("small", "large")))
async def provide_dungeon_description(callback: types.CallbackQuery, state: FSMContext):
    if callback.data in ("small", "large"):
        await state.update_data(size=callback.data)
        size = callback.data
    else:
        size = await state.get_value("size")
    language = await state.get_value("language")
    dungeon = get_dungeon(size, language)
    dungeon_description = dungeon[0]
    dungeon_dict = dungeon[1]
    # Store dungeon content for future use
    await state.update_data(dungeon=dungeon_dict)

    await callback.message.answer(
        dungeon_description,
        reply_markup=keyboards.proceed.get_keyboard(language)
    )
    await state.set_state(fsm.GenerateDungeon.proceed_or_retry)


# Generate areas -> Retry or back
@r.callback_query(fsm.GenerateDungeon.proceed_or_retry, F.data == "proceed")
async def get_areas(callback: types.CallbackQuery, state: FSMContext):
    language = await state.get_value("language")
    dungeon_dict = await state.get_value("dungeon")
    dungeon = Dungeon(dungeon_dict)
    areas = dungeon.get_areas()

    # Создать лист
    areas_list = []
    # Проитерировать по словарям, превратив каждую пару k, v в строку
    for area_key, area_content in areas.items():
        for item, value in area_content.items():
            if isinstance(value, Creature):
                area_content[item] = value.kind + ", " + value.disposition
        content = content_to_str(area_content, language)
        area_header = localize_area_header(language)
        areas_list.append(f"{area_header} #{area_key}:\n{content}")
    
    text = "\n\n".join(areas_list)

    language = await state.get_value("language")
    await callback.message.answer(
        text,
        reply_markup=keyboards.confirmation.get_keyboard(language)
    )
    await state.set_state(fsm.GenerateDungeon.confirmation)


# Retry -> Generate dungeon description again
@r.callback_query(fsm.GenerateDungeon.proceed_or_retry, F.data == "retry")
async def get_description_again(callback: types.CallbackQuery, state: FSMContext):
    await provide_dungeon_description(callback, state)


# Generate areas once more -> New areas
@r.callback_query(fsm.GenerateDungeon.confirmation, F.data == "over_generate")
async def get_areas_again(callback: types.CallbackQuery, state: FSMContext):
    await get_areas(callback, state)
