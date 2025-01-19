import data
from dungeon_generation.pre_generation.pre_generation import (get_creatures,
                                                              get_objects,
                                                              get_rewards,
                                                              get_traps,
                                                              get_items)

import random


def generate(size: str):
    # Decode dungeon size:
    if size == "small":
        area_limit = random.randint(5, 7)
    else:
        area_limit = random.randint(9, 12)

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

    # Define creatures could be met in the dungeon
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

    # Compose string with traps (if any)
    traps = get_traps(area_limit, current_condition)
    if traps:
        traps_str = "- " + "\n- ".join(traps)
    else:
        traps_str = "-"

    # Compose findings (items) string
    # Main items to be given first, additional only if necessary
    main_items, additional_items = get_items(area_limit, function, ruination).values()
    items_str = ("Основные предметы:\n- %s\n"
                 "Дополнительные предметы:\n- %s"
                 % ("\n- ".join(main_items), "\n- ".join(additional_items)))

    # Compose string with objects to find
    objects_list = get_objects(function, area_limit)
    objects = "- " + "\n- ".join(objects_list)

    # Compose string with reward(s)
    rewards = get_rewards(size, builder, function)
    rewards_str = f"Награда(ы): {tuple(s for s in rewards)}"

    # Compose dungeon description string
    desc_str = ("Dungeon:\n"
                "Size: %s\n"
                "Area limit: %i\n"
                "Built by: %s\n"
                "Function: %s\n"
                "Ruined by: %s\n"
                "Current condition: %s\n"
                "\n"
                "Main creatures to meet: \n%s\n"
                "Additional creatures to meet: \n%s\n"
                "Boss: %s\n"
                "Ловушки: \n%s\n"
                "%s\n"  # Предметы
                "Возможные объекты:\n%s\n"
                "%s"  # Награды
                % (size, area_limit, builder, function, ruination, current_condition,
                   main_creatures, additional_creatures, boss, traps_str, items_str,
                   objects, rewards_str)
                )
    return desc_str
