def kto255(r:int, g:int, b:int):
    k = 0
    if r not in range(0, 255):
        raise ValueError(f'r not in range 0-255. r = {r}')
    elif g not in range(0, 255):
        raise ValueError(f'g not in range 0-255. g = {g}')
    elif b not in range(0, 255):
        raise ValueError(f'b not in range 0-255. b = {b}')
    
    if r == 0 and g == 0 and b == 0:
        raise ValueError('Cannot process perfect black')
    elif r >= g:
        if r >= b:
            if r != 0:
                k = (r/255)
    if g >= r:
        if g >= b:
            if g != 0:
                k = (g/255)
    if b >= r:
        if b >= g:
            if b != 0:
                k = (b/255)
    return(round(r/k), round(g/k), round(b/k))
    
def mto255(r:int, g:int, b:int):
    m = 0
    if r not in range(0, 255):
        raise ValueError(f'r not in range 0-255. r = {r}')
    elif g not in range(0, 255):
        raise ValueError(f'g not in range 0-255. g = {g}')
    elif b not in range(0, 255):
        raise ValueError(f'b not in range 0-255. b = {b}')
        
    if r == 0 and g == 0 and b == 0:
        raise ValueError('Cannot process perfect black')
    elif r >= g:
        if r >= b:
            if r != 0:
                m = (255-r)
    if g >= r:
        if g >= b:
            if g != 0:
                m = (255-r)
    if b >= r:
        if b >= g:
            if b != 0:
                m = (255-b)
    return(round(r+m), round(g+m), round(b+m))