import data

import random
import math
from typing import Any

MIN_AREA_NUM = 5


class Creature:
    def __init__(self, creature_obj):
        self.kind = creature_obj["kind"]
        self.disposition_list = creature_obj["disposition"]
        self.alignments = creature_obj["alignment"]  # TODO: использовать или удалить
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


def get_creatures(area_limit: int, condition: str, language: str) -> dict:
    """Define creatures to meet in dungeon
       :param area_limit: number of areas in dungeon
       :param condition: current condition of dungeon
       :param language: Language chosen by user
       :return: dict[str: (Creature,), str: (Creature,), str: Creature].
            Dict contains main creatures tuple, additional creatures tuple and boss Creature object.
    """
    creatures = None
    if condition in ("заселено монстрами", "inhabited by monsters"):
        creatures = set_monsters_populated_creatures(area_limit, language)
    elif condition in ("исследование", "exploration"):
        creatures = set_exploration_creatures(area_limit, language)
    elif condition in ("оккупировано", "occupied"):
        creatures = set_occupied_creatures(area_limit, language)
    elif condition in ("противостояние", "confrontation"):
        creatures = set_confrontation_creatures(area_limit, language)
    if not creatures:
        print("Error: unsupported dungeon current condition")
        quit(1)
    return creatures


def set_monsters_populated_creatures(area_limit: int, language:str) -> dict:
    main_creature_num = int(area_limit / 4)
    main_creature_options = [Creature(kind) for kind
                             in data.MONSTERS[language] if kind["prevalence"] in ("uncommon", "rare")]
    main_creatures = random.sample(main_creature_options, k=main_creature_num)
    additional_creature_options_hybrids = [Creature(kind) for kind
                                           in data.HUMANOID_HYBRIDS[language]]
    additional_creature_options_humanoids = [Creature(kind) for kind
                                             in data.HUMANOIDS[language] if not kind["civilized"]]
    additional_creature_options_monsters = [Creature(kind) for kind
                                            in data.MONSTERS[language]]
    additional_creature_options = (additional_creature_options_hybrids
                                   + additional_creature_options_humanoids
                                   + additional_creature_options_monsters)
    additional_creature_num = int(1 + area_limit / 5)
    additional_creatures = random.sample(additional_creature_options, k=additional_creature_num)
    is_boss = random.choice([True, False])
    if not is_boss:
        boss = None
    else:
        boss = Creature(random.choice(data.BOSSES[language]))

    creatures = {"main_creatures": main_creatures,
                 "additional_creatures": additional_creatures,
                 "boss": boss}
    return creatures


def set_exploration_creatures(area_limit: int, language: str) -> dict:
    main_creature_num = int(1 + (area_limit / 5.5))
    main_creature_group = [Creature(kind) for kind
                           in data.MONSTERS[language] if not kind["sociality"] == "solitary"]
    main_creatures = [random.choice(main_creature_group)]
    main_creature_num -= 1
    if main_creature_num > 0:
        main_creature_options = [Creature(kind) for kind
                                 in data.MONSTERS[language]]
        main_creature_add = random.sample(main_creature_options,
                                          k=main_creature_num)
        for el in main_creature_add:
            main_creatures.append(el)
    additional_creature_options = [Creature(kind) for kind
                                   in data.HUMANOIDS[language] if kind["civilized"]]
    additional_creature_num = int(area_limit / 3.5)
    additional_creatures = random.sample(additional_creature_options, k=additional_creature_num)
    boss = Creature(random.choice(data.BOSSES[language]))
    creatures = {"main_creatures": main_creatures,
                 "additional_creatures": additional_creatures,
                 "boss": boss}
    return creatures


def set_occupied_creatures(area_limit: int, language: str) -> dict:
    main_creature_options = [Creature(kind) for kind
                             in data.HUMANOIDS[language]]
    main_creatures = [random.choice(main_creature_options)]
    additional_creature_beasts = [Creature(kind) for kind
                                  in data.BEASTS[language]]
    additional_creature_uncommon_rare = [Creature(kind) for kind
                                         in data.MONSTERS[language] if kind["prevalence"] in ("uncommon", "rare")]
    additional_creature_legendary = random.sample([Creature(kind) for kind
                                                   in data.MONSTERS[language] if kind["prevalence"] == "legendary"],
                                                  # To have lesser chance of legendary
                                                  k=int((len(data.MONSTERS[language]) / 4))
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
        boss = Creature(random.choice(data.BOSSES[language]))
    creatures = {"main_creatures": main_creatures,
                 "additional_creatures": additional_creatures,
                 "boss": boss}
    return creatures


def set_confrontation_creatures(area_limit: int, language: str) -> dict:
    main_creature_civilized = [Creature(kind) for kind
                               in data.HUMANOIDS[language] if kind["civilized"]]
    main_creature_wild = [Creature(kind) for kind
                          in data.HUMANOIDS[language] if not kind["civilized"]]
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
                                  in data.BEASTS[language]]
    additional_creature_monsters = [Creature(kind) for kind
                                    in data.MONSTERS[language] if kind["prevalence"] in ("uncommon", "rare")]
    additional_creature_legendary = random.sample([Creature(kind) for kind
                                                   in data.MONSTERS[language] if kind["prevalence"] == "legendary"],
                                                  # To have lesser chance of legendary
                                                  k=int((len(data.MONSTERS[language]) / 4))
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


def get_objects(function: str, area_limit: int, language: str) -> list:
    unique_options = []
    for el in data.OBJECTS[language]:
        if function in el["functions"]:
            unique_options.append(el)
    common_options = []
    for el in data.OBJECTS[language]:
        if "universal" in el["functions"] and el not in unique_options:
            common_options.append(el)
    n_unique = int(area_limit / 5.5) + 1
    n_common = int(area_limit / 4)
    objects_unique = random.sample(unique_options, n_unique)
    objects_common = random.sample(common_options, n_common)
    objects = ([unique["description"] for unique in objects_unique]
               + [common["description"] for common in objects_common])
    return objects


def get_rewards(size: str, builder: str, function: str, language: str) -> tuple:
    options = []
    for el in data.REWARDS[language]:
        if builder in el["builders"] and function in el["functions"]:
            options.append(el["description"])
    if size == "small":
        rewards = (random.choice(options),)
    elif size == "large":
        if len(options) == 1:
            # Если всего 1 подходящая награда (должно быть 2)
            rewards = (options[0], options[0])
        else:
            rewards = tuple(random.sample(options, 2))
    return rewards


def get_traps(area_limit: int, condition: str, language: str) -> Any:
    if condition in ("заселено монстрами", "inhabited by monsters"):
        return False
    elif condition in ("оккупировано", "occupied"):
        k = 3
    elif condition in ("противостояние", "confrontation"):
        k = 2.5
    elif condition in ("исследование", "exploration"):
        k = 4

    traps_num = int(area_limit / k)
    options = [trap["description"] for trap in data.TRAPS[language]]
    traps = random.sample(options, traps_num)
    return traps


def get_items(area_limit, function: str, ruination: str, language: str) -> dict:
    """Define items to be found: main and additional.
       Items with corresponding both function and ruination
       have higher chance to be chosen.
    """
    options_high_chance = [item["description"] for item
                           in data.DISCOVERIES_FIND[language]
                           if function in item["functions"]
                           and ruination in item["ruinations"]]
    options_low_chance = [item["description"] for item
                          in data.DISCOVERIES_FIND[language]
                          if function in item["functions"]
                          or ruination in item["ruinations"]]
    items = {"main": choose_main_items(area_limit,
                                       options_high_chance,
                                       options_low_chance),
             "additional": choose_additional_items(area_limit,
                                                   options_high_chance,
                                                   options_low_chance)
             }
    return items


def choose_main_items(area_limit: int,
                      options_high_chance: list,
                      options_low_chance: list
                      ) -> list:
    num = math.floor((area_limit * 0.6) + 0.5)  # Для округл. к ближ. целому
    options = [options_high_chance, options_low_chance]
    r_option = random.choices(options, [2, 1])[0]
    if num > len(r_option):
        # Избегаем ошибки 'ValueError: Sample larger than population or is negative'
        num = len(r_option)
    main_items = random.sample(r_option, num)
    return main_items


def choose_additional_items(area_limit: int,
                            options_high_chance,
                            options_low_chance
                            ) -> list:
    num = round(area_limit * 0.7)
    options = [options_high_chance, options_low_chance]
    # Fix ValueError 'sample larger than population' for sample()
    population = random.choices(options, [1.2, 1])[0]
    if num > len(population):
        return population
    # Otherwise return sample
    additional_items = random.sample(population, num)
    return additional_items
