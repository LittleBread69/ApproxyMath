from functools import cache

@cache
def fact(x: int | float) -> int | float:
    if type(x) not in [int, float]:
        raise TypeError("Not accepted")
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    isFloat = isinstance(x, float)
    if x <= 1.0:
        return x if isFloat else 1

    result = x * fact(x - 1)
    return float(result) if isFloat else int(result)
