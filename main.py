import data
from helpers import get_themes_number, get_area_limit_number
from themes_generator import generate_themes
from areas_generator import generate_area

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
    themes = generate_themes(themes_number, size)

    # Construct response string
    s = ("Dungeon #1:\n" 
         "Size: %s\n" 
         "Area limit: %i\n" 
         "Built by %s\n" 
         "Function: %s\n" 
         "Ruined by: %s\n" 
         "Themes & countdowns:"
         % (size, area_limit, builder, function, ruination))

    # Append string with themes
    for theme in themes:
        s = '\n'.join([s, f"- {theme.name}: {theme.countdown}"])

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
    unique_areas_num = int(area_limit / 2)
    common_areas_num = int((area_limit - unique_areas_num - 1) / 2.5) + 1  # Improvised formula
    print("Write down %i+ common areas and %i unique areas aligning with dungeon themes. \n"
          "Roll or choose one of them every time you need to present a new area.\n"
          % (common_areas_num, unique_areas_num))

    # Generate new random area
    new_area = generate_area(themes)

    # Compose discoveries string
    if not new_area[2]:
        # No discoveries
        discoveries_str = " -"
    else:
        # Compose list of discoveries
        discoveries_str = ""
        for discovery in new_area[2]:
            discoveries_str = "\n- ".join([discoveries_str, discovery])

    # TODO: Compose dangers string
    if not new_area[3]:
        # No dangers
        dangers_str = " -"
    else:
        # Compose list of dangers
        dangers_str = ""
        for danger in new_area[3]:
            dangers_str = "\n- ".join([dangers_str, danger])

    # Provide area description
    print(
        "Type: %s\n"
        "Theme: %s\n"
        "Discoveries:"
        "%s\n"
        "Dangers:"
        "%s"
        % (new_area[1], new_area[0], discoveries_str, dangers_str)
    )


if __name__ == "__main__":
    main()
