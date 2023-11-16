from math import log as logn

lnsqrt_constant = 0.6137056388802

def ln(x:float) -> float:
    return logn(x)

def ln_rt(x:float, lnsqrt:float=lnsqrt_constant) -> float:
    return logn(x) + lnsqrt