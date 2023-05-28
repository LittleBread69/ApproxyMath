def apxsqrt(x: int):
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number :({}".format(x) + ")")
    if x == 0:
        return 0
    if x > 0:
        if x ** 0.5 % 1 == 0:
            return int(x ** 0.5)
        else:
            y = x
            w = 0
            while w ** 2 < y:
                w += 1
            if w ** 2 > y:
                w -= 1
            y = w + (x - w ** 2) / (2 * w)
            if y ** 2 == (w + 1) ** 2:
                return y - 0.06
            else:             
                return y

def prcsqrt(x: float):
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number: ({}".format(x) + ")")
    else:
        return x ** 0.5
