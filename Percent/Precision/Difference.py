from functools import cache

@cache
def differences(experimental_val:float, theorique_val:float) -> float:
    return (abs(theorique_val - experimental_val) / theorique_val) * 100
