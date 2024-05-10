import data

import random
from typing import Any

MIN_AREA_NUM = 5

def roll_d6(n=1) -> int:
    """Roll 1d6 n times and add results"""
    result = sum(random.randint(1,6) for _ in range(n))
    return result


def roll_d12() -> int:
    """Roll 1d12"""
    return random.randint(1,12)


class Creature:
    def __init__(self, creature_obj):
        self.kind = creature_obj["kind"]
        self.disposition_list = creature_obj["disposition"]
        self.alignments = creature_obj["alignment"]
        self.disposition = None

    def set_disposition(self) -> None:
        """Define disposition to players' characters"""
        length = len(self.disposition_list)
        # Set higher probability for aggressive disposition
        probabilities = [2] + [1] * (length - 1)
        self.disposition, = random.choices(self.disposition_list, probabilities)

    def check_if_civilized(self):
        civilized_humanoids = [creature["kind"] for creature
                               in data.HUMANOIDS if creature["civilized"]]
        if self.kind in civilized_humanoids:
            return True
        return False


def get_creatures(area_limit: int, condition: str) -> dict:
    """Define creatures to meet in dungeon
    :param area_limit: number of areas in dungeon
    :param condition: current condition of dungeon
    """
    creatures = None
    if condition == "заселено монстрами":
        creatures = set_monsters_populated_creatures(area_limit)
    elif condition == "исследование":
        creatures = set_exploration_creatures(area_limit)
    elif condition == "оккупировано":
        creatures = set_occupied_creatures(area_limit)
    elif condition == "противостояние":
        creatures = set_confrontation_creatures(area_limit)
    if not creatures:
        print("Error: not supported dungeon current condition")
        quit(1)
    return creatures


def set_monsters_populated_creatures(area_limit: int) -> dict:
    main_creature_num = int(area_limit / 4)
    main_creature_options = [Creature(kind) for kind
                             in data.MONSTERS if kind["prevalence"] in ("uncommon", "rare")]
    main_creatures = random.sample(main_creature_options, k=main_creature_num)
    additional_creature_options_hybrids = [Creature(kind) for kind
                                           in data.HUMANOID_HYBRIDS]
    additional_creature_options_humanoids = [Creature(kind) for kind
                                             in data.HUMANOIDS if not kind["civilized"]]
    additional_creature_options_monsters = [Creature(kind) for kind
                                            in data.MONSTERS]
    additional_creature_options = (additional_creature_options_hybrids
                                   + additional_creature_options_humanoids
                                   + additional_creature_options_monsters)
    additional_creature_num = int(1 + area_limit / 5)
    additional_creatures = random.sample(additional_creature_options, k=additional_creature_num)
    is_boss = random.choice([True, False])
    if not is_boss:
        boss = None
    else:
        boss = Creature(random.choice(data.BOSSES))

    creatures = {"main_creatures": main_creatures,
                 "additional_creatures": additional_creatures,
                 "boss": boss}
    return creatures


def set_exploration_creatures(area_limit: int) -> dict:
    main_creature_num = int(1 + (area_limit / 5.5))
    main_creature_group = [Creature(kind) for kind
                           in data.MONSTERS if not kind["sociality"] == "solitary"]
    main_creatures = [random.choice(main_creature_group)]
    main_creature_num -= 1
    if main_creature_num > 0:
        main_creature_options = [Creature(kind) for kind
                                 in data.MONSTERS]
        main_creature_add = random.sample(main_creature_options,
                                          k=main_creature_num)
        for el in main_creature_add:
            main_creatures.append(el)
    additional_creature_options = [Creature(kind) for kind
                                   in data.HUMANOIDS if kind["civilized"]]
    additional_creature_num = int(area_limit / 3.5)
    additional_creatures = random.sample(additional_creature_options, k=additional_creature_num)
    boss = Creature(random.choice(data.BOSSES))
    creatures = {"main_creatures": main_creatures,
                 "additional_creatures": additional_creatures,
                 "boss": boss}
    return creatures


def set_occupied_creatures(area_limit: int) -> dict:
    main_creature_options = [Creature(kind) for kind
                             in data.HUMANOIDS]
    main_creatures = [random.choice(main_creature_options)]
    additional_creature_beasts = [Creature(kind) for kind
                                  in data.BEASTS]
    additional_creature_uncommon_rare = [Creature(kind) for kind
                                         in data.MONSTERS if kind["prevalence"] in ("uncommon", "rare")]
    additional_creature_legendary = random.sample([Creature(kind) for kind
                                                   in data.MONSTERS if kind["prevalence"] == "legendary"],
                                                  k=int((len(data.MONSTERS) / 4))  # To have lesser chance of legendary
                                                  )
    additional_creature_options = (additional_creature_beasts
                                   + additional_creature_uncommon_rare
                                   + additional_creature_legendary)
    additional_creature_num = 1 + int(area_limit / 4)
    additional_creatures = random.sample(additional_creature_options, k=additional_creature_num)
    is_boss = random.choice([True, False])
    if not is_boss:
        boss = None
    else:
        boss = Creature(random.choice(data.BOSSES))
    creatures = {"main_creatures": main_creatures,
                 "additional_creatures": additional_creatures,
                 "boss": boss}
    return creatures


def set_confrontation_creatures(area_limit: int) -> dict:
    main_creature_civilized = [Creature(kind) for kind
                               in data.HUMANOIDS if kind["civilized"]]
    main_creature_wild = [Creature(kind) for kind
                          in data.HUMANOIDS if not kind["civilized"]]
    # Make it possible to meet 3 main confronting kind of creatures
    main_3_creatures = None
    if area_limit >= 10:
        main_3_creatures = random.choices([True, False], weights=[1, 2])
    if main_3_creatures:
        n = 2
    else:
        n = 1

    main_creatures = [random.choice(main_creature_civilized),
                      *random.sample(main_creature_wild, k=n)]
    additional_creature_beasts = [Creature(kind) for kind
                                  in data.BEASTS]
    additional_creature_monsters = [Creature(kind) for kind
                                    in data.MONSTERS if kind["prevalence"] in ("uncommon", "rare")]
    additional_creature_legendary = random.sample([Creature(kind) for kind
                                                   in data.MONSTERS if kind["prevalence"] == "legendary"],
                                                  k=int((len(data.MONSTERS) / 4))  # To have lesser chance of legendary
                                                  )
    additional_creature_options = (additional_creature_beasts
                                   + additional_creature_monsters
                                   + additional_creature_legendary)
    additional_creature_num = int(area_limit / 4.5)
    additional_creatures = random.sample(additional_creature_options, k=additional_creature_num)
    creatures = {"main_creatures": main_creatures,
                 "additional_creatures": additional_creatures,
                 "boss": None}
    return creatures


def get_objects(function: str, area_limit: int) -> list:
    unique_options = []
    for el in data.OBJECTS:
        if function in el["functions"]:
            unique_options.append(el)
    common_options = []
    for el in data.OBJECTS:
        if "universal" in el["functions"] and el not in unique_options:
            common_options.append(el)
    n_unique = int(area_limit / 5.5) + 1
    n_common = int(area_limit / 4)
    objects_unique = random.sample(unique_options, n_unique)
    objects_common = random.sample(common_options, n_common)
    objects = ([unique["description"] for unique in objects_unique]
               + [common["description"] for common in objects_common])
    return objects


def get_rewards(size: str, builder: str, function: str) -> str:
    options = []
    for el in data.REWARDS:
        if builder in el["builders"] and function in el["functions"]:
            options.append(el["description"])
    if size == "small":
        rewards = random.choice(options)
    elif size == "large":
        rewards = ", ".join(random.sample(options, 2))
    return rewards


def get_traps(area_limit: int, condition: str) -> Any:
    if condition == "заселено монстрами":
        return False
    elif condition == "оккупировано":
        k = 3
    elif condition == "противостояние":
        k = 2.5
    elif condition == "исследование":
        k = 4

    traps_num = int(area_limit / k)
    options = [trap["description"] for trap in data.TRAPS]
    traps = random.sample(options, traps_num)
    return traps
