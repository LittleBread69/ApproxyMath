from functools import cache

@cache
def apxsqrt(x: int) -> float:
    if x < 0:
        raise ValueError(f"Cannot compute the square root of a negative number :({x})")
    elif x == 0:
        return 0
    #else
    w = 0
    if (x ** 0.5) % 1 == 0:
        return int(x ** 0.5)
    y = x
    while w * w < y:
        w += 1
    if w ** 2 > y:
        w -= 1
    y = w + (x - w * w) / (2 * w)
    if x == 3:
        return y - (4/15)
    elif y ** 2 == (w + 1) ** 2:
        return y - 0.06          
    return y

def prcsqrt(x: float):
    if x < 0:
        raise ValueError(f"Cannot compute the square root of a negative number: ({x})")
    else:
        return x ** 0.5
