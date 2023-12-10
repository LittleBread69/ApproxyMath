def floor(x:float) -> int:
    if x >= 0:
        return int(x)
    return int(x)-1

def ceil(x:float) -> int:
    if x>=0:
        return int(x)+1
    return int(x)