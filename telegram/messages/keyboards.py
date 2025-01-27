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
        builder.adjust(1)  # По 1 кнопке в ряд
        return builder.as_markup()


# Выбор языка
choose_language = Keyboard(
    [InlineKeyboardButton(text="Английский", callback_data="english"),
     InlineKeyboardButton(text="Русский", callback_data="russian")],
    [InlineKeyboardButton(text="English", callback_data="english"),
     InlineKeyboardButton(text="Русский", callback_data="russian")],
)


# Выбор размера подземелья
choose_size = Keyboard(
    [InlineKeyboardButton(text="Малый", callback_data="small"),
     InlineKeyboardButton(text="Большой", callback_data="large")],
    [InlineKeyboardButton(text="Small", callback_data="small"),
     InlineKeyboardButton(text="Large", callback_data="large")],
)

# Сгенерировать области или попробовать еще раз
proceed = Keyboard(
    [InlineKeyboardButton(text="Сгенерировать области", callback_data="proceed"),
     InlineKeyboardButton(text="Попробовать еще раз", callback_data="retry"),
     InlineKeyboardButton(text="Назад", callback_data="back")],
    [InlineKeyboardButton(text="Generate areas", callback_data="proceed"),
     InlineKeyboardButton(text="Try again", callback_data="retry"),
     InlineKeyboardButton(text="Back", callback_data="back")],
)

# Выбор после генерации областей
confirmation = Keyboard(
    [InlineKeyboardButton(text="Переделать области", callback_data="retry"),
     InlineKeyboardButton(text="Начать сначала", callback_data="back")],
    [InlineKeyboardButton(text="Try other areas", callback_data="proceed"),
     InlineKeyboardButton(text="Start over", callback_data="back")],
)
