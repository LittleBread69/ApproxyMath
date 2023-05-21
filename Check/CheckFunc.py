astr = [' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'x', '^', '+', '-']

def checkFunc(f: str):
    c = 0
    af = []
    for i in f:
        af.append(i)
        c += 1
        if af[c-1] not in astr:
            raise ValueError("Char '" + str(af[c-1]) + "' not supported.")
    if af[0] == ' ':
        raise ValueError("The function cannot start with a blank space.")