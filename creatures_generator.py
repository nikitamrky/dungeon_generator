import data
from helpers import roll_d12

import random


class Creature:

    def __init__(self,
                 creature_type,
                 name,
                 activity,
                 alignment,
                 disposition,
                 num,
                 ability,
                 equipment
                 ):
        self.creature_type = creature_type
        self.name = name
        self.activity = activity
        self.alignment = alignment
        self.disposition = disposition
        self.num = num
        self.ability = ability
        self.equipment = equipment


def new_creature():
    """Create new Creature object"""
    r = roll_d12()

    if r <= 4:
        creature_type = "beast"
    elif r <= 6:
        creature_type = "human"
    elif r <= 8:
        creature_type = "humanoid"
    else:
        creature_type = "monster"
