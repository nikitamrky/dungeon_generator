import data
from helpers import roll_d12, get_themes_number

import random


class Theme:

    def __init__(self, name, countdown):
        self.name = name
        self.countdown = countdown

    def mark(self):
        self.countdown -= 1
        if self.countdown == 0:
            return False
        else:
            return True


def get_theme() -> str:
    """Choose random theme"""

    r = roll_d12()

    # Return mundane theme if r from 1 to 5
    if r <= 5:
        return random.choice(data.THEMES_MUNDANE)

    # Return unusual theme if r from 6 to 9
    elif r <= 9:
        return random.choice(data.THEMES_UNUSUAL)

    # Return extraordinary theme if r from 10 to 12
    else:
        return random.choice(data.THEMES_EXTRAORDINARY)


def generate_themes(number, size) -> list:
    themes = []
    for i in range(number):
        theme_name = get_theme()
        theme_countdown = get_themes_number(size)
        themes.append(Theme(theme_name, theme_countdown))
    return themes
