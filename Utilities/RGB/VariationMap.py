from numpy import sin, pi, sqrt
import numpy as np

def VariatePixelColour(x:float) -> float:
    return ((((0.28846153846153844 * (sin(sqrt(x))) ** 3) * (12 / sin(sqrt(x))) * sin(6 * x) - sin(2 * x) + 17.5) ** 0.6766696666435431) / 8)
