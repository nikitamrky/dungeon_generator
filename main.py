import data
from helpers import get_themes_number, get_theme

import random


def main():

    # Define all dungeon meta data variables except themes
    size = random.choice(data.SIZES)
    builder = random.choice(data.FOUNDATION_BUILDERS)
    function = random.choice(data.FOUNDATION_FUNCTIONS)
    ruination = random.choice(data.RUINATIONS)

    # Define number of themes
    themes_number = get_themes_number(size)

    # Generate themes
    themes = []
    for i in range (themes_number):
        themes.append(get_theme())

    # Construct response string
    s = ("Dungeon #1:\n" \
        "Size: %s\n" \
        "Builded by %s\n" \
        "Function: %s\n" \
        "Ruined by: %s\n" \
        "Themes:" \
         % (size, builder, function, ruination))

    # Append string with themes
    for theme in themes:
        s = '\n'.join([s, "- %s" % theme])

    # Print result
    print(s)


if __name__ == "__main__":
    main()
