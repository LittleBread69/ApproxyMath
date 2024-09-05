import math
from functools import cache

@cache
def Viete(a, b, c) -> tuple[int|float, int|float]|None:
    delta = b * b - 4 * a * c
    if delta >= 0:
        return (-b - math.sqrt(delta)) / (2 * a), (-b + math.sqrt(delta)) / (2 * a)
    return None

@cache
def SimpleViete(b, c) -> tuple[int|float, int|float]|None:
    delta = b * b - 4 * c
    if delta >= 0:
        return (-b - math.sqrt(delta)) / 2, (-b + math.sqrt(delta)) / 2
    return None

@cache
def Muller(a, b, c, positive=True)-> tuple[int|float, int|float]|None:
    delta = b * b - 4 * a * c
    if delta >= 0:
        if positive:
            return -2 * c / (b - math.sqrt(delta)), -2 * c / (b + math.sqrt(delta))
        return 2 * c / (- b + math.sqrt(delta)), 2 * c / (-b - math.sqrt(delta))
    return None
