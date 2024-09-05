from functools import cache

@cache
def xrootx(x:float|int|str) -> float|int:
    if x == 'max':
        return xrootx(2.718)
    elif type(x) != str:
        return x ** (1/x)
    
