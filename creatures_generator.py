import data
from helpers import roll_d12

import random


class Creature:

    def __init__(self,
                 creature_type,
                 creature_subtype,
                 name,
                 num,
                 # activity,
                 # alignment,
                 # disposition,
                 # ability,
                 # equipment,
                 ):
        self.creature_type = creature_type
        self.creature_subtype = creature_subtype
        self.name = name
        self.num = num
        # self.activity = activity
        # self.alignment = alignment
        # self.disposition = disposition
        # self.ability = ability
        # self.equipment = equipment


def new_creature() -> Creature:
    """Create new Creature object"""

    # Define creature type and subtype
    creature_type = get_creature_type()
    creature_subtype = get_creature_subtype(creature_type)

    # Get random creature
    creature_data = get_random_creature(creature_subtype)

    # Define creature name
    creature_name = creature_data[0]

    # Define number appearing
    num = get_creature_num(creature_data)

    # activity = random.choice(data.ACTIVITY)
    # alignment = random.choice(data.ALIGNMENT)
    # disposition = random.choice(data.DISPOSITION)

    creature = Creature(creature_type, creature_subtype, creature_name, num)
    return creature


def get_creature_type() -> str:
    r = roll_d12()
    if r <= 3:
        creature_type = "beast"
    elif r <= 5:
        creature_type = "human"
    elif r <= 8:
        creature_type = "humanoid"
    else:
        creature_type = "monster"

    return creature_type


def get_creature_subtype(creature_type: str) -> str:
    if creature_type == "beast":
        creature_subtype = get_beast_subtype()
    elif creature_type == "human":
        creature_subtype = None
    elif creature_type == "humanoid":
        creature_subtype = get_humanoid_subtype()
    else:
        creature_subtype = get_monster_subtype()

    return creature_subtype


def get_beast_subtype() -> str:
    r = roll_d12()
    if r <= 9:
        beast_subtype = "earthbound"
    else:
        beast_subtype = "airborne"
    return beast_subtype
    # TODO: add water-going (optional for user)
    # r = roll_d12()
    # if r <= 7: beast_subtype = "earthbound"
    # elif r <= 10: beast_subtype = "airborne"
    # else: beast_subtype = "water-going"
    # return beast_subtype


def get_humanoid_subtype() -> str:
    r = roll_d12()
    if r <= 7:
        humanoid_subtype = "common"
    elif r <= 10:
        humanoid_subtype = "uncommon"
    else:
        humanoid_subtype = "hybrid"
    return humanoid_subtype


def get_monster_subtype() -> str:
    r = roll_d12()
    if r <= 7:
        monster_subtype = "unusual"
    elif r <= 10:
        monster_subtype = "rare"
    else:
        monster_subtype = "legendary"
    return monster_subtype


def get_random_creature(creature_subtype: str or None) -> tuple:
    if not creature_subtype:
        creature_data = random.choice(data.HUMAN)
        return creature_data
    if creature_subtype == "earthbound":
        creature_data = random.choice(data.BEAST_EARTHBOUND)
    elif creature_subtype == "airborne":
        creature_data = random.choice(data.BEAST_AIRBORNE)
    # elif creature_subtype == "water-going":
    #     creature_data = random.choice(data.BEAST_WATERGOING)
    elif creature_subtype == "common":
        creature_data = random.choice(data.HUMANOID_COMMON)
    elif creature_subtype == "uncommon":
        creature_data = random.choice(data.HUMANOID_UNCOMMON)
    elif creature_subtype == "hybrid":
        creature_data = random.choice(data.HUMANOID_HYBRID)
    elif creature_subtype == "unusual":
        creature_data = random.choice(data.MONSTER_UNUSUAL)
    elif creature_subtype == "rare":
        creature_data = random.choice(data.MONSTER_RARE)
    else:
        creature_data = random.choice(data.MONSTER_LEGENDARY)
    return creature_data


def get_creature_num(creature: tuple) -> int:
    if "solitary" in creature[1]:
        num = random.choice([1, 1, 1, 2])
    elif "group" in creature[1]:
        num = random.choice([
            random.randint(1, 2),
            random.randint(3, 6)
        ])
    elif "horde" in creature[1]:
        r = roll_d12()
        if r <= 2:
            num = r
        elif r <= 9:
            num = random.randint(3, 7)
        elif r <= 11:
            num = random.randint(8, 15)
        else:
            num = random.randint(15, 30)
    else:  # "swarm" in creature[1]
        r = roll_d12()
        if r == 1:
            num = 1
        elif r <= 5:
            num = random.randint(2, 10)
        elif r <= 10:
            num = random.randint(11, 25)
        else:
            num = random.randint(26, 50)
    return num
