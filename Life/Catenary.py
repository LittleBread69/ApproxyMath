from numba import njit
from numpy import cosh

perfect_a = 6.1875922777425565e-1

@njit(fastmath=True)
def Catenary(x:float, a:float = perfect_a) -> float:
    return a * cosh(x/a) - a

@njit(fastmath=True)
def Bridge(x: float, a:float = perfect_a) -> float:
    return -(a * cosh(x/a) - a)
