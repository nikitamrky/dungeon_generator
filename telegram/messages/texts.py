class TextData:

    def __init__(self, text_ru, text_eng):
        self._text_ru = text_ru
        self._text_eng = text_eng

    def get_text(self, language="eng"):
        if language == "ru":
            return self._text_ru
        else:
            return self._text_eng


# Выбрать размер подземелья
choose_language = TextData(
    "Выбери язык",
    "Choose language"
)


# Выбрать размер подземелья
choose_size = TextData(
    "Выбери размер подземелья",
    "Choose dungeon size"
)


# Для формирования описания подземелья
dungeon_size = TextData(
    "Размер",
    "Size"
)
dungeon_areas_num = TextData(
    "Комнат (областей)",
    "Areas"
)
dungeon_builder = TextData(
    "Кем построено",
    "Built by"
)
dungeon_function = TextData(
    "Функция",
    "Function"
)
dungeon_ruination = TextData(
    "Причина упадка",
    "Ruined by"
)
dungeon_condition = TextData(
    "Текущее состояние",
    "Current condition"
)
dungeon_main_creatures = TextData(
    "Основные существа",
    "Main creatures"
)
dungeon_additional_creatures = TextData(
    "Возможные существа",
    "Optional creatures"
)
dungeon_boss = TextData(
    "Босс",
    "Boss"
)
dungeon_traps = TextData(
    "Ловушки",
    "Traps"
)
dungeon_main_items = TextData(
    "Основные находки",
    "Main findings"
)
dungeon_additional_items = TextData(
    "Дополнительные находки",
    "Additional findings"
)
dungeon_objects = TextData(
    "Объекты в подземелье",
    "Objects in dungeon"
)
dungeon_rewards = TextData(
    "Главная награда(ы)",
    "Big reward(s)"
)