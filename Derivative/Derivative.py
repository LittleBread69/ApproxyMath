from Check.CheckFunc import checkFunc as cFnc
##Doesn't work currently.
def tan(func: str):
    f = func
    af = []
    if f == 'help' or f == 'h':
        pass
    else:
        cFnc(f)
        return f
