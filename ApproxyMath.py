from SquareRoot.SqrtApprox import *
from Pi.Pi import *
p_pi = lenpi(4)
from Chemistry.AcidAndBases import *
from Absolute.AprxAbs import *
from Percent.Variations.PerVar import *
from Euler_Neper.e import *
p_e = lene(6)
from SquareRoot.SqrtConst import *
from Utilities.Shorter.Shorten import *
from Utilities.Other.Utils import *
from Utilities.RGB.RGB_Tools import *
from Biology.Genetics import *
from HW.ScreenUtils.AspectRatio import *
from Life.Catenary import *
from Euler_Neper.ln import *
from Fibonacci.fibonacci import *
from Specific_Equations.xrootx import *
from Trigonometry.cos_sin_tan import *
from Random.arandom import *
from Linear_and_Quadratic.Quadratic import *
from Linear_and_Quadratic.Linear import *
from Utilities.list_utils.list_flattening import *
from Percent.Precision.Difference import *

def help():
    with open("help.txt") as helf:
        helt = ''.join(helf.readlines())
        print(helt)

def commands():
    with open("commands.txt") as comf:
        comt = ''.join(comf.readlines())
        print(comt)