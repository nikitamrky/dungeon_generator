import data
from helpers import roll_d12

import random


def get_discoveries() -> list:
    """Generate discoveries"""
    discoveries = []
    r = roll_d12()
    if r <= 3:
        discoveries.append(random.choice(data.DISCOVERIES_DRESSING))
    elif r <= 9:
        discoveries.append(random.choice(data.DISCOVERIES_FEATURE))
    else:
        temp = random.choice(data.DISCOVERIES_FIND)
        if not temp == "roll twice":
            discoveries.append(temp)
        else:
            # Roll twice for "FIND" type of discovery, but w/o "roll twice" again
            for i in range(2):
                discoveries.append(data.DISCOVERIES_FIND[random.randint(0, 10)])
    return discoveries


def get_dangers() -> list:  # TODO
    dangers = []
    r = roll_d12()
    if r <= 4:
        temp = random.choice(data.DANGERS_TRAP)
        if not temp == "roll twice":
            dangers.append("trap: " + temp)
        else:
            for i in range(2):
                dangers.append("trap: " + data.DANGERS_TRAP[random.randint(0, 10)])
    elif r <= 11:
        dangers.append("creature")
    else:
        dangers.append(random.choice(data.DANGERS_ENTITY))
    return dangers


def generate_area(themes: list) -> tuple:
    """Generate area: theme (considering countdown),
    type (common/uncommon), discoveries and dangers.

    :param themes: list of Theme objects.
    """
    # Get area types and content (quantitative)
    area_content = random.choice(data.AREA_CONTENT)

    # Define theme
    if area_content[0] == "unthemed":
        theme = "unthemed"
    else:
        theme = "themed"  # TODO: choose theme from countdowns

    # Define type (common/uncommon)
    area_type = area_content[1]

    # Define discoveries
    if not area_content[2]:
        discoveries = None
    else:
        discoveries = (get_discoveries())

    # Define dangers
    if not area_content[3]:
        dangers = None
    else:
        dangers = (get_dangers())

    area = (theme, area_type, discoveries, dangers)
    return area
