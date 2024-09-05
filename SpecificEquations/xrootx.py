from functools import cache

@cache
def xrootx(x:float|int|str) -> float|int|None: #type:ignore
    if x == 'max':
        return xrootx(2.718)
    elif type(x) in [int, float]:
        return (x ** (1/x)) #type:ignore
    return