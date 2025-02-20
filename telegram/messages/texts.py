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
