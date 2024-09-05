from functools import cache

@cache
def differences(experimental_val:float, theoric_val:float) -> float:
    return (abs(theoric_val - experimental_val) / theoric_val) * 100
