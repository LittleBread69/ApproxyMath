from random import randint

def randfloat(floatrange:tuple[float, float]=(0,1),norange:bool=True) -> float|int:
    x = randint(0, 2 ** 63 - 1) / (2 ** 63 - 1)
    if norange:
        return x
    return x * (floatrange[1] - floatrange[0]) + floatrange[0]