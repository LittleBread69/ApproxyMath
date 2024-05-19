
def fact(x:int|float) -> int|float:
    if type(x) != int and type(x) != float: raise TypeError("Not accepted")
    isFloat = False if type(x) == int else True
    if x < 1.0: return x
    result:float|int = 1.0
    return fact(n-1) * n
    return float(result) if isFloat else int(result)
