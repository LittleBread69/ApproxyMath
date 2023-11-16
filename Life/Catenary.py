from math import cosh
perfect_a = 6.1875922777425565e-1

def Catenary(x:float, a:float = perfect_a) -> float:
    return a * cosh(x/a) - a

def Bridge(x: float, a:float = perfect_a) -> float:
    return -(a * cosh(x/a) - a)
