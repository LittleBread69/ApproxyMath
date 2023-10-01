from math import sin, cos, pi

def Abs(x: float) -> float:
    return float(x*(x>=0)-x*(x<0))

def InfAbs(x: float, mode:str = 'prs') -> float:
    supported_modes = ['sin', 'prs']
    if mode not in supported_modes:
        raise ValueError(f"Mode {mode} not supported. Please choose one from these: {supported_modes}.")
    else:  
        return ((abs(cos(x*(pi/2)))-abs(sin(x*(pi/2))) + 1)/2)*(mode=='sin') + (int(x%2) + ((x-int(x))*(int(x)%2==0) - (x-(int(x)))*int(int(x)%2==1)))*(mode=='prs')

