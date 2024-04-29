
def fact(x:int|float) -> int|float:
    result:float|int = x
    while x > 1:
        result *= x
        x -= 1
    return result
