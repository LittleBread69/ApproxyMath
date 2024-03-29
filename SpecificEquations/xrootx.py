from functools import lru_cache as lcache

@lcache
def xrootx(x:float|int|str) -> float|int: #type:ignore
    if x == 'max':
        return xrootx(2.718)
    elif type(x) != str:
        return x ** (1/x) #type:ignore
    
