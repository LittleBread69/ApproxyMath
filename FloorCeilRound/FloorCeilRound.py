def floor(x:float) -> int:
    if x >= 0 or x-int(x)==0:
        return int(x)
    return int(x)-1

def ceil(x:float) -> int:
    if x>=0 and x - int(x)!=0:
        return int(x)+1
    return int(x)