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


