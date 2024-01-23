import data

import random


def get_themes_number(size: str) -> int:
    """Generate number of themes as well as theme countdowns"""

    # Return 1d4 dice result if dungeon size is small
    if size.lower() == "small":
        return random.randint(1, 4)

    # Define a constant term (k) corresponding to dungeon size
    if size.lower() == "medium": k = 0
    elif size.lower() == "large": k = 1
    else: k = 2

    # Calculate and return result (1d6 + k)
    return random.randint(1,6) + k


def roll_d6(n=1) -> int:
    """Roll 1d6 n times and add results"""
    result = sum(random.randint(1,6) for _ in range(n))
    return result


def roll_d12() -> int:
    """Roll 1d12"""
    return random.randint(1,12)


def get_theme() -> str:
    """Generate random theme"""

    r = roll_d12()

    # Return mundane theme if r from 1 to 5
    if r <= 5:
        return random.choice(data.THEMES_MUNDANE)

    # Return unusual theme if r from 6 to 9
    elif r <= 9:
        return random.choice(data.THEMES_UNUSUAL)

    # Return extraordinary theme if r from 10 to 12
    else:
        return random.choice(data.THEMES_EXTRAORDINARY)


def get_area_limit_number(size: str) -> int:
    """Generate area limit for dungeon"""

    # Define coefficient for 1d6 dice (a) and constant term (k)
    if size.lower() == "small":
        a = 1
        k = 2
    elif size.lower() == "medium":
        a = 2
        k = 4
    elif size.lower() == "large":
        a = 3
        k = 6
    else:
        a = 4
        k = 10

    # Calculate and return the number of areas
    n = roll_d6(a) + k
    return n
