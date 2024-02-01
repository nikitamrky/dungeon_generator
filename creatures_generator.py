import data
from helpers import roll_d12

import random


class Creature:

    def __init__(self,
                 creature_type,
                 creature_subtype,
                 name,
                 activity,
                 alignment,
                 disposition,
                 num,
                 ability,
                 equipment
                 ):
        self.creature_type = creature_type
        self.creature_subtype = creature_subtype
        self.name = name
        self.activity = activity
        self.alignment = alignment
        self.disposition = disposition
        self.num = num
        self.ability = ability
        self.equipment = equipment


def new_creature() -> Creature:
    """Create new Creature object"""

    # Define creature type and subtype
    creature_type = get_creature_type()
    creature_subtype = get_creature_subtype(creature_type)

    # Define creature name
    creature_name = get_creature_name(creature_subtype)

    # Define creature activity
    activity = random.choice(data.ACTIVITY)

    # Define creature alignment
    if creature_type == "beast":
        alignment = None
    else:
        alignment = random.choice(data.ALIGNMENT)

    # TODO: relate disposition to alignment: only good, neutral or lawful can be hopeful
    # Define creature disposition
    disposition = random.choice(data.DISPOSITION)


def get_creature_type() -> str:
    r = roll_d12()
    if r <= 4:
        creature_type = "beast"
    elif r <= 6:
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
    if r <= 7:
        beast_subtype = "earthbound"
    elif r <= 10:
        beast_subtype = "airborne"
    else:
        beast_subtype = "water-going"
    return beast_subtype


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


def get_creature_name(creature_subtype: str or None) -> str:
    if not creature_subtype:
        creature_name = "human"
        return creature_name
    r = roll_d12()
    if creature_subtype == "earthbound":
        creature_name = random.choice(data.BEAST_EARTHBOUND)
    elif creature_subtype == "airborne":
        creature_name = random.choice(data.BEAST_AIRBORNE)
    elif creature_subtype == "water-going":
        creature_name = random.choice(data.BEAST_WATERGOING)
    elif creature_subtype == "common":
        creature_name = random.choice(data.HUMANOID_COMMON)
    elif creature_subtype == "uncommon":
        creature_name = random.choice(data.HUMANOID_UNCOMMON)
    elif creature_subtype == "hybrid":
        creature_name = random.choice(data.HUMANOID_HYBRID)
    elif creature_subtype == "unusual":
        creature_name = random.choice(data.MONSTER_UNUSUAL)
    elif creature_subtype == "rare":
        creature_name = random.choice(data.MONSTER_RARE)
    else:
        creature_name = random.choice(data.MONSTER_LEGENDARY)
    return creature_name

