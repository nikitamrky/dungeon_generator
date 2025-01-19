from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


class Keyboard:

    def __init__(self, buttons_ru, buttons_eng):
        self._buttons_ru = buttons_ru
        self._buttons_eng = buttons_eng

    def get_keyboard(self, language=str):
        # TODO: получать язык из контекста, а не из аргументов вызова
        if language not in ("ru", "eng"):
            language = "eng"

        builder = InlineKeyboardBuilder()
        buttons = None
        if language == "ru":
            buttons = self._buttons_ru
        elif language == "eng":
            buttons = self._buttons_eng

        for button in buttons:
            builder.add(
                InlineKeyboardButton(
                    text=button.text,
                    callback_data=button.callback_data
                )
            )

        return builder.as_markup()


# Выбор размера подземелья
choose_size = Keyboard(
    [InlineKeyboardButton(text="Малый", callback_data="small"),
     InlineKeyboardButton(text="Большой", callback_data="large")],
    [InlineKeyboardButton(text="Small", callback_data="small"),
     InlineKeyboardButton(text="Large", callback_data="large")],
)
