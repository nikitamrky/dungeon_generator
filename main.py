import data
from helpers import get_creatures

import random


def main():

    # Get dungeon size from user
    while True:
        temp = input("Выберите размер подземелья: s (small) или l (large): ")
        if temp in ("s", "l"):
            break

    # Decode dungeon size:
    if temp == "s":
        size = "small"
        area_limit = random.randint(5, 7)
    else:
        size = "large"
        area_limit = random.randint(8, 12)

    # Define builder(s)
    builder = random.choice(data.FOUNDATION_BUILDERS)

    # Define old function of the place
    functions = [function["description"] for function
                 in data.FOUNDATION_FUNCTIONS if builder in function["builders"]]
    function = random.choice(functions)

    # Define cause of ruination
    ruination = random.choice(data.RUINATIONS)

    # Define current condition
    conditions = [condition["description"] for condition
                  in data.CURRENT_CONDITIONS if ruination in condition["ruinations"]]
    current_condition = random.choice(conditions)

    # Define what creatures could be met in the dungeon
    creatures = get_creatures(area_limit, current_condition)

    # Compose strings for creatures
    main_creatures = ", ".join(creatures["main_creatures"])
    additional_creatures = ", ".join(creatures["additional_creatures"])
    boss = creatures["boss"] or None

    # Construct dungeon description string
    s = ("Dungeon:\n" 
         "Size: %s\n" 
         "Area limit: %i\n" 
         "Built by: %s\n" 
         "Function: %s\n" 
         "Ruined by: %s\n" 
         "Current condition: %s\n"
         "Main creatures to meet: %s\n"
         "Additional creatures to meet: %s\n"
         "Boss: %s\n"
         % (size, area_limit, builder, function, ruination, current_condition,
            main_creatures, additional_creatures, boss)
         )

    # Print result
    print(s)


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
