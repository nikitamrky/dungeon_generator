class TextData:

    def __init__(self, text_ru, text_eng):
        self._text_ru = text_ru
        self._text_eng = text_eng

    def get_text_ru(self):
        return self._text_ru

    def get_text_eng(self):
        return self._text_eng


# Выбрать размер подземелья
choose_size = TextData(
    "Выбери размер подземелья",
    "Choose dungeon size"
)
