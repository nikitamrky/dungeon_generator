import old_data
from helpers import get_area_limit_number

import random


def main():
    # Define all dungeon meta data variables except themes
    size = random.choice(data.SIZES)
    area_limit = get_area_limit_number(size)
    builder = random.choice(data.FOUNDATION_BUILDERS)
    function = random.choice(data.FOUNDATION_FUNCTIONS)
    ruination = random.choice(data.RUINATIONS)
    # TODO: current_condition = random.choice

    # Construct response string
    s = ("Dungeon #1:\n" 
         "Size: %s\n" 
         "Area limit: %i\n" 
         "Built by %s\n" 
         "Function: %s\n" 
         "Ruined by: %s\n" 
         "Themes & countdowns:"
         % (size, area_limit, builder, function, ruination))

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

    # Generate new random area
    # new_area = generate_area()

    # Compose discoveries string
    # if not new_area[2]:
    #     # No discoveries
    #     discoveries_str = " -"
    # else:
    #     # Compose list of discoveries
    #     discoveries_str = ""
    #     for discovery in new_area[2]:
    #         discoveries_str = "\n- ".join([discoveries_str, discovery])

    # Compose dangers string
    # if not new_area[3]:
    #     # No dangers
    #     dangers_str = " -"
    # else:
    #     # Compose list of dangers
    #     dangers_str = ""
    #     for danger in new_area[3]:
    #         # Concatenate if trap
    #         if isinstance(danger, str):
    #             dangers_str = "\n- ".join([dangers_str, danger])
    #         # Extract name and attrs if creature:
    #         else:
    #             creature_str = f"{danger.name} ({danger.num})"
    #             dangers_str = "\n- ".join([dangers_str, creature_str])

    # Provide area description
    # print(
    #     "Type: %s\n"
    #     "Theme: %s\n"
    #     "Discoveries:"
    #     "%s\n"
    #     "Dangers:"
    #     "%s"
    #     % (new_area[1], new_area[0], discoveries_str, dangers_str)
    # )


if __name__ == "__main__":
    main()
