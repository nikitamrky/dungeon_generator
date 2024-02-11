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

    # Set dispositions for creatures
    for creature in creatures["main_creatures"]:
        creature.set_disposition()
    for creature in creatures["additional_creatures"]:
        creature.set_disposition()
    if creatures["boss"]:
        creatures["boss"].set_disposition()

    # Compose string with creatures descriptions for...
    # ... main creatures
    main_creatures = "- "
    print()  # Test code
    main_creatures_content = [f"{creature.kind} ({creature.disposition})"
                              for creature in creatures["main_creatures"]]
    main_creatures += "\n- ".join(main_creatures_content)
    # ... additional creatures
    additional_creatures = "- "
    additional_creatures_content = [f"{creature.kind} ({creature.disposition})"
                              for creature in creatures["additional_creatures"]]
    additional_creatures += "\n- ".join(additional_creatures_content)
    # ... boss
    if not creatures["boss"]:
        boss = "нет"
    else:
        boss = ("%s (%s)"
                % (creatures["boss"].kind, creatures["boss"].disposition))

    # Construct dungeon description string
    s = ("Dungeon:\n" 
         "Size: %s\n" 
         "Area limit: %i\n" 
         "Built by: %s\n" 
         "Function: %s\n" 
         "Ruined by: %s\n" 
         "Current condition: %s\n"
         "Main creatures to meet: \n%s\n"
         "Additional creatures to meet: \n%s\n"
         "Boss: %s\n"
         % (size, area_limit, builder, function, ruination, current_condition,
            main_creatures, additional_creatures, boss)
         )

    # Print result
    print(s)


if __name__ == "__main__":
    main()
