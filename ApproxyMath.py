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
#from pprint import pprint 
from Biology.Genetics import *
from HW.ScreenUtils.AspectRatio import *

def help():
    print("ApproxyMath is small and polyvalent math (and other) approximation library.")
    print("Type 'Commands()' to get a list of all the commands and what they do.")
    print("Please read the documentation for more informations.")

def commands():
    print("LIST of COMMANDS:")
    print('\n'+"aprxAbs()\n    Approximates the absolute value of any float.\n")
    print('lene()\n'+"    Custom lenght of the Euleur number: e.\n")