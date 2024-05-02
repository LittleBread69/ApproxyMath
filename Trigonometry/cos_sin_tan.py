
def sin(x:float) -> float:
    if x < 0 or x > 1:
        raise ValueError(f"the approximation of sin only works with values between 0 and 1, input={x}")
    else: 
        return x
