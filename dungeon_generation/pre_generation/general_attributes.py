import data
from dungeon_generation.pre_generation.pre_generation import (get_creatures,
                                                              get_objects,
                                                              get_rewards,
                                                              get_traps,
                                                              get_items)

import random


def generate(size: str):
    """
    Provide dungeon description as string and as dictionary.
    :param size: Dungeon size.
    :return: Кортеж из 2 элементов:
        - str: Полное описание контента подземелья.
        - dict: Словарь с контентом для последующего использования.
    """
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

    traps = get_traps(area_limit, current_condition)
    main_items, additional_items = get_items(area_limit, function, ruination).values()
    objects = get_objects(function, area_limit)
    rewards = get_rewards(size, builder, function)

    # Compose dungeon description object
    dungeon_dict = {"size": size,
                    "area_limit": area_limit,
                    "builder": builder,
                    "function": function,
                    "ruination": ruination,
                    "current_condition": current_condition,
                    "main_creatures": creatures["main_creatures"],
                    "additional_creatures": creatures["additional_creatures"],
                    "boss": creatures["boss"],
                    "traps": traps,
                    "items": (main_items, additional_items),
                    "objects": objects,
                    "rewards": rewards}
    dungeon_str = dungeon_to_str(dungeon_dict)

    return dungeon_str, dungeon_dict


def dungeon_to_str(dungeon_attrs: dict):
    # Compose main creatures string
    main_creatures_str = "- "
    main_creatures_content = [f"{creature.kind}: {creature.disposition}"
                              for creature in dungeon_attrs["main_creatures"]]
    main_creatures_str += "\n- ".join(main_creatures_content)
    # Compose additional creatures string
    additional_creatures_str = "- "
    additional_creatures_content = [f"{creature.kind} ({creature.disposition})"
                                    for creature in dungeon_attrs["additional_creatures"]]
    additional_creatures_str += "\n- ".join(additional_creatures_content)
    # Compose boss string
    if not dungeon_attrs["boss"]:
        boss_str = "-"
    else:
        boss_str = ("%s (%s)"
                % (dungeon_attrs["boss"].kind, dungeon_attrs["boss"].disposition))
    # Compose traps string
    if dungeon_attrs["traps"]:
        traps_str = "- " + "\n- ".join(dungeon_attrs["traps"])
    else:
        traps_str = "-"
    # Compose items  string
    items_str = ("Основные предметы:\n- %s\n"
                 "Дополнительные предметы:\n- %s"
                 % ("\n- ".join(dungeon_attrs["items"][0]),
                    "\n- ".join(dungeon_attrs["items"][1])))
    # Objects and rewards strings
    objects_str = "- " + "\n- ".join(dungeon_attrs["objects"])
    rewards_str = f"{', '.join(dungeon_attrs['rewards'])}"
    # Final string
    description = ("Dungeon:\n"
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
                   "Награда(ы): %s"
                   % (dungeon_attrs["size"],
                      dungeon_attrs["area_limit"],
                      dungeon_attrs["builder"],
                      dungeon_attrs["function"],
                      dungeon_attrs["ruination"],
                      dungeon_attrs["current_condition"],
                      main_creatures_str,
                      additional_creatures_str,
                      boss_str,
                      traps_str,
                      items_str,
                      objects_str,
                      rewards_str,)
                   )
    return description
