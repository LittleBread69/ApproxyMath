from numpy import log as logn

lnsqrt_constant = 0.6137056388802

def ln(x:float) -> float:
    return logn(x)

def ln_rt(x:float) -> float:
    return logn(x) + lnsqrt_constant