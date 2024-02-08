import old_data

import random


def roll_d6(n=1) -> int:
    """Roll 1d6 n times and add results"""
    result = sum(random.randint(1,6) for _ in range(n))
    return result


def roll_d12() -> int:
    """Roll 1d12"""
    return random.randint(1,12)


def get_area_limit_number(size: str) -> int:
    """Generate area limit for dungeon"""
    # Define coefficient for 1d6 dice (a) and constant term (k)
    if size.lower() == "small":
        n = random.randint(4, 7)
    else:
        n = random.randint(8, 11)
    return n