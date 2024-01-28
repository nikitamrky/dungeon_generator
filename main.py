import data
from helpers import get_themes_number, get_theme, get_area_limit_number

import random


def main():
    # Define all dungeon meta data variables except themes
    size = random.choice(data.SIZES)
    area_limit = get_area_limit_number(size)
    builder = random.choice(data.FOUNDATION_BUILDERS)
    function = random.choice(data.FOUNDATION_FUNCTIONS)
    ruination = random.choice(data.RUINATIONS)

    # Define number of themes
    themes_number = get_themes_number(size)

    # Generate themes
    themes = []
    for i in range(themes_number):
        countdown = get_themes_number(size)
        themes.append(get_theme() + ": %s" % countdown)

    # Construct response string
    s = ("Dungeon #1:\n" \
         "Size: %s\n" \
         "Area limit: %i\n" \
         "Builded by %s\n" \
         "Function: %s\n" \
         "Ruined by: %s\n" \
         "Themes & countdowns:" \
         % (size, area_limit, builder, function, ruination))

    # Append string with themes
    for theme in themes:
        s = '\n'.join([s, "- %s" % theme])

    # Print result
    print(s)

    # Ask if user confirms dungeon meta data
    while True:
        proceed = input("Do you want to proceed with this dungeon? [y/n]: ")
        if "n" in proceed.lower():
            quit(1)  # TODO: chatbot will offer another dungeon
        elif not "y" in proceed.lower():
            pass
        else:
            break

    # Reminder to compose unique areas list
    print("Write down %i unique areas aligning with dungeon themes. \n"
          "Roll or choose one of them every time you need to present a unique area.\n"
          % (int(area_limit / 2)))

    # TODO: offer some options to exclude (e.g. water-going creatures) via button menu

    # Generate new random area


if __name__ == "__main__":
    main()
