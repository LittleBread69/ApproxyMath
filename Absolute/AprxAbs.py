from math import sin, cos, pi

def Abs(x: float|int) -> float|int:
    return float(x*(x>=0)-x*(x<0))

def InfAbs(x: float|int, mode:str = 'prs') -> float|int:
    supported_modes = ['sin', 'prs']
    if mode not in supported_modes:
        raise ValueError(f"Mode {mode} not supported. Please choose one from these: {supported_modes}.")
    elif mode == 'sin':
        return (abs(cos(x * (pi / 2))) - abs(sin(x * (pi / 2))) + 1) / 2
    #else
    return int(x % 2) + ((x - int(x)) * (int(x) % 2 == 0) - (x - (int(x))) * int(int(x) % 2 == 1))
