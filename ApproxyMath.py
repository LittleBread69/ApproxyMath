from SquareRoot.SqrtApprox import *
#from Derivative.Derivative import *
from Pi.Pi import *
p_pi = lenpi(4)
from Chemistry.AcidAndBases import *
from Absolute.AprxAbs import *
from Variations.PerVar import *
from Euler.e import *
p_e = lene(6)
c_e = ecalc(16777216)
from SquareRoot.SqrtConst import *
from Utilities.Shorter.Shorten import *
from Utilities.Other.Utils import *
from Utilities.RGB.RGB_Tools import *
from pprint import pprint 

def help():
    pprint("ApproxyMath is small and polyvalent math (and other) approximation library.")
    pprint("Type 'Commands()' to get a list of all the commands and what they do.")
    pprint("Please read the documentation for more informations.")

def commands():
    pprint("LIST of COMMANDS:")
    pprint('\n'+"aprxAbs()\n    Approximates the absolute value of any float.\n")
    pprint('lene()\n'+"    Custom lenght of the Euleur number: e.\n")

pprint(shorten(InfAbs(8.4), 14))
pprint(InfAbs(8.4, 'sin'))