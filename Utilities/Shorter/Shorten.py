from Euler.e import lene
from Pi.Pi import lenpi

def eshort(length: int) -> float:
    return lene(length)

def pishort(lenght: int) -> float:
    return lenpi(lenght)

def shorten(value: float, lenght: int) -> float:
    return round(value, lenght)