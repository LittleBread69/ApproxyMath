from random import uniform

def OOvar(value: float, variation: int) -> float | int:
    #percent variations
    vl = value
    vr = variation
    
    vl += uniform(0, (vr/100))
    vl -= uniform(0, (vr/100))
    
    return vl

def OOOvar(value: float, variation: int) -> float | int:
    #permile variations
    vl = value
    vr = variation
    
    vl += uniform(0, (vr/1000))
    vl -= uniform(0, (vr/1000))
    
    return vl