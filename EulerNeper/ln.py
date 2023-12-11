from math import log as logn

lnsqrt_constant = 0.6137056388802
klnsqrt_constant = 0.824360635350065

def ln(x:float) -> float:
    return logn(x)

def ln_rt(x:float, lnsqrt:float=lnsqrt_constant) -> float:
    return logn(x) + lnsqrt

def kln_rt(x:float, klnsqrt:float=klnsqrt_constant) -> float:
    return klnsqrt * logn(x) + klnsqrt