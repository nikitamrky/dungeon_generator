from telegram.messages.texts import localize_area_key


def content_to_str(content: dict, language: str) -> str:
    """
    Converts area content to a string.
    :param content: dict with content of a single area
    :param language: language of user's choice
    :return: formatted string
    """
    fu = ""
    for key, value in content.items():
        foo = f"- {localize_area_key(key, language)}: {value}\n"
        fu += foo
    fu = fu.strip()

    return fu


def size_localize(size: str, language: str) -> str:
    if size == "small":
        if language == "eng":
            return size
        elif language == "ru":
            return "малый"
        else:
            print("Error: unsupported language")
            quit(1)
    elif size == "large":
        if language == "eng":
            return size
        elif language == "ru":
            return "большой"
        else:
            print("Error: unsupported language")
            quit(1)
    else:
        print("Error: unsupported dungeon size")
        quit(1)


def localize_area_header(language: str) -> str:
    if language == "eng":
        return "Area"
    elif language == "ru":
        return "Область"
    else:
        print("Error: unsupported language")
        quit(1)
