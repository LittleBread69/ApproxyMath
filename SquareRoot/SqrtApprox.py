def apxsqrt(x: int):
    #print("x = " + str(x))
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number :({}".format(x) + ")")
    if x == 0:
        return 0
    if x > 0:
        if x ** 0.5 % 1 == 0:
            return int(x ** 0.5)
        else:
            w = 0
            while w ** 2 < x:
                w += 1
            if w ** 2 > x:
                w -= 1
            x = w + (x - w ** 2) / (2 * w)
            if x ** 2 == (w + 1) ** 2:
                return x - 0.05
            else:             
                return x

def prcsqrt(x: float or int):
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number: ({}".format(x) + ")")
    else:
        return x ** 0.5
    
#print(apxsqrt(-14))
#print(apxsqrt(100))
#print(apxsqrt(48))
#print(apxsqrt(39))
#print(apxsqrt(87))
#print(apxsqrt)

#print(prcsqrt)