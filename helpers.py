import data

import random


def roll_d6(n=1) -> int:
    """Roll 1d6 n times and add results"""
    result = sum(random.randint(1,6) for _ in range(n))
    return result


def roll_d12() -> int:
    """Roll 1d12"""
    return random.randint(1,12)


def get_creatures(area_limit: int, condition: str) -> dict:
    if condition == "заселено монстрами":
        creatures = set_monster_invasion_creatures(area_limit, condition)
    elif condition == "исследование":
        creatures = set_exploration_creatures(area_limit, condition)
    elif condition == "оккупировано":
        creatures = set_occupied_creatures(area_limit, condition)
    elif condition == "противостояние":
        creatures = set_confrontation_creatures(area_limit, condition)
    if not creatures:
        print("Error: not supported dungeon current condition")
        quit(1)
    return creatures


def set_monster_invasion_creatures(area_limit: int, condition: str) -> dict:
    main_creature_num = int(area_limit / 4)
    main_creature_options = [creature["kind"] for creature
                             in data.MONSTERS if creature["prevalence"] in ("uncommon", "rare")]
    main_creatures = [random.choice(main_creature_options)
                      for _ in range(main_creature_num)]
    additional_creature_options_hybrids = [creature["kind"] for creature
                                           in data.HUMANOID_HYBRIDS]
    additional_creature_options_humanoids = [creature["kind"] for creature
                                             in data.HUMANOIDS if not creature["civilized"]]
    additional_creature_options_monsters = [creature["kind"] for creature
                                            in data.MONSTERS if creature["prevalence"] == "legendary"]
    additional_creature_options = (additional_creature_options_hybrids
                                   + additional_creature_options_humanoids
                                   + additional_creature_options_monsters)
    additional_creature_num = int(area_limit / 5)
    additional_creatures = [random.choice(additional_creature_options)
                            for _ in range(additional_creature_num)]
    is_boss = random.choice([True, False])
    if not is_boss:
        boss = None
    else:
        boss = random.choice(data.BOSSES)["kind"]

    creatures = {"main_creatures": main_creatures,
                 "additional_creatures": additional_creatures,
                 "boss": boss}
    return creatures


def set_exploration_creatures(area_limit: int, condition: str) -> dict:
    main_creature_num = int(area_limit / 5.5)
    main_creature_options = [creature["kind"] for creature
                            in data.MONSTERS if creature["prevalence"] in ("uncommon", "rare")]
    main_creatures = [random.choice(main_creature_options)
                           for _ in range(main_creature_num)]
    additional_creature_options = [creature["kind"] for creature
                                   in data.HUMANOIDS if creature["civilized"]]
    additional_creature_num = int(area_limit / 5)
    additional_creatures = [random.choice(additional_creature_options)
                            for _ in range(additional_creature_num)]
    boss = random.choice(data.BOSSES)["kind"]
    creatures = {"main_creatures": main_creatures,
                 "additional_creatures": additional_creatures,
                 "boss": boss}
    return creatures

def set_occupied_creatures(area_limit: int, condition: str) -> dict:
    main_creature_options = [creature["kind"] for creature
                             in data.HUMANOIDS]
    main_creatures = [random.choice(main_creature_options)]
    additional_creature_beasts = [creature["kind"] for creature
                                  in data.BEASTS]
    additional_creature_uncommon_rare = [creature["kind"] for creature
                                         in data.MONSTERS if creature["prevalence"] in ("uncommon", "rare")]
    additional_creature_legendary = [creature["kind"] for creature
                                     in data.MONSTERS if creature["prevalence"] == "legendary"]
    additional_creatures = [random.choice(additional_creature_uncommon_rare),
                            random.choice(additional_creature_legendary)]
    is_boss = random.choice([True, False])
    if not is_boss:
        boss = None
    else:
        boss = random.choice(data.BOSSES)["kind"]
    creatures = {"main_creatures": main_creatures,
                 "additional_creatures": additional_creatures,
                 "boss": boss}
    return creatures


def set_confrontation_creatures(area_limit: int, condition: str) -> dict:
    main_creature_options_civilized = [creature["kind"] for creature
                                       in data.HUMANOIDS if creature["civilized"]]
    main_creature_options_wild = [creature["kind"] for creature
                                  in data.HUMANOIDS if not creature["civilized"]]
    main_creatures = [random.choice(main_creature_options_civilized),
                      random.choice(main_creature_options_wild)]
    additional_creature_options_beasts = [creature["kind"] for creature
                                          in data.BEASTS]
    additional_creature_options_monsters = [creature["kind"] for creature
                                            in data.MONSTERS if creature["prevalence"] in ("uncommon", "rare")]
    additional_creature_options = (additional_creature_options_beasts
                                   + additional_creature_options_monsters)
    additional_creature_num = int(area_limit / 5)
    additional_creatures = [random.choice(additional_creature_options)
                            for _ in range(additional_creature_num)]
    creatures = {"main_creatures": main_creatures,
                 "additional_creatures": additional_creatures,
                 "boss": None}
    return creatures
