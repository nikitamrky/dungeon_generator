from aiogram.fsm.state import StatesGroup, State


class MainMenu(StatesGroup):
    choosing_language = State()


class GenerateDungeon(StatesGroup):
    choosing_size = State()
    proceed_or_retry = State()
    confirmation = State()