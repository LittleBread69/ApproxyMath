from functools import lru_cache
import sys

@lru_cache(512)
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

if __name__ == '__main__':
    print(fact(2))
    print(fact(2.0))
    print(fact(0.3))
    print(fact(22))