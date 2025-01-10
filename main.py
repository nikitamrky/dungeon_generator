from settings import get_settings
from telegram.bot import run_bot

from temp_logic import temp_func


def main():

    # Собрать переменные среды и настройки для запуска приложения
    # TODO
    settings = get_settings()

    # Запустить приложение
    # TODO
    run_bot(settings)

    # TODO: удалить реликтовую функцию и файл temp_logic
    temp_func()


if __name__ == "__main__":
    main()
