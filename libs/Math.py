import numpy as np
import math as mat
import cmath as ctm
import warnings
from sympy import trigsimp
from scipy import integrate
from scipy import fft
warnings.filterwarnings("ignore")
np.seterr(all='warn')
nan=mat.nan
Inf=mat.inf
def Integrate(x,y):
    return(integrate.fixed_quad(x,y,None))
def FFT(y,z):
    return(fft(y,z))
def TrigSimp(y):
    return(trigsimp(y))
def Transltr(val0):
    if isinstance(val0,(float,int)):
        return val0
    else:
        try:
            ans=eval(val0.replace('"', '').replace("'", ''))
            for a in ans:
                if isinstance(a,(int,float)):
                    return a
                else:
                    return ans
        except:
            return float(val0.replace('"', '').replace("'", ''))
        #finally:
         #   return str(val0.replace('"', '').replace("'", ''))
def Negate(val1):
    try:
        return -val1
    except:
        for item in val1:
            try:
                b=-float(item)
                return b
            except:
                return 1       
def Minus(x, y):
    if isinstance(x, str):
        x = Transltr(x)
    if isinstance(y, str):
        y = Transltr(y)
    if isinstance(x, list) or isinstance(y, list):
        if isinstance(x, (float, int)):
            x = [x] * len(y)
        if isinstance(y, (float, int)):
            y = [y] * len(x)
        try:
            return [a - b for a, b in zip(x, y)]
        except:
            return x - y
    else:
        return x - y

def Plus(x, y):
    if isinstance(x, str):
        x = Transltr(x)
    if isinstance(y, str):
        y = Transltr(y)
    if isinstance(x, list) or isinstance(y, list):
        if isinstance(x, (float, int)):
            x = [x] * len(y)
        if isinstance(y, (float, int)):
            y = [y] * len(x)
        try:
            return [a + b for a, b in zip(x, y)]
        except:
            return x + y
    else:
        return x + y

def Times(x, y):
    if isinstance(x, str):
        x = Transltr(x)
    if isinstance(y, str):
        y = Transltr(y)
    if isinstance(x, list) or isinstance(y, list):
        if isinstance(x, (float, int)):
            x = [x] * len(y)
        if isinstance(y, (float, int)):
            y = [y] * len(x)
        try:
            return [a * b for a, b in zip(x, y)]
        except:
            return x * y
    else:
        return x * y

def Power(x, y):
    if isinstance(x, str):
        x = Transltr(x)
    if isinstance(y, str):
        y = Transltr(y)
    if isinstance(x, list) or isinstance(y, list):
        if isinstance(x, (float, int)):
            x = [x] * len(y)
        if isinstance(y, (float, int)):
            y = [y] * len(x)
        return [a ** b for a, b in zip(x, y)]
    else:
        return x ** y

def Divide(x, y):
    if isinstance(x, str):
        x = Transltr(x)
    if isinstance(y, str):
        y = Transltr(y)
    if isinstance(x, list) or isinstance(y, list):
        if isinstance(x, (float, int)):
            x = [x] * len(y)
        if isinstance(y, (float, int)):
            y = [y] * len(x)
        return [a / b if b != 0 else np.nan for a, b in zip(x, y)]
    else:
        return (x / y) if y !=0 else np.nan

def Maximum(x, y):
    if isinstance(x, str):
        x = Transltr(x)
    if isinstance(y, str):
        y = Transltr(y)
    if isinstance(x, list) or isinstance(y, list):
        if isinstance(x, (float, int)):
            x = [x] * len(y)
        if isinstance(y, (float, int)):
            y = [y] * len(x)
        return max([max(a,b) for a, b in zip(x, y)])
    else:
        return max(x, y)

def Minimum(x, y):
    if isinstance(x, str):
        x = Transltr(x)
    if isinstance(y, str):
        y = Transltr(y)
    if isinstance(x, list) or isinstance(y, list):
        if isinstance(x, (float, int)):
            x = [x] * len(y)
        if isinstance(y, (float, int)):
            y = [y] * len(x)
        return min([min(a, b) for a, b in zip(x, y)])
    else:
        return min(x, y)

def Atan2r(x, y):
    if isinstance(x, str):
        x = Transltr(x)
    if isinstance(y, str):
        y = Transltr(y)
    if isinstance(x, list) or isinstance(y, list):
        if isinstance(x, (float, int)):
            x = [x] * len(y)
        if isinstance(y, (float, int)):
            y = [y] * len(x)
        return [np.arctan2(np.real(a), np.real(b)) for a, b in zip(x, y)]
        #return [np.arctan2(np.real(a), np.real(b)) if isinstance(a, complex) and isinstance(b, complex) else np.nan for a, b in zip(x, y)]
    else:
        return np.arctan2(np.real(x), np.real(y)) #if isinstance(x, complex) and isinstance(y, complex) else np.nan

def Sqrt(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
     #   return np.sqrt(z)
    return [np.sqrt(a) for a in z] if isinstance(z, list) else np.sqrt(z) #if isinstance(z, complex) else np.nan

def Sqr(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    return z ** 2
    return [a ** 2 for a in z] if isinstance(z, list) else z ** 2

def Logn(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    try:
    #        return np.real(ctm.log(z))
    #    except:
    #        return np.nan
    return [np.real(ctm.log(a)) if isinstance(a, complex) else np.nan for a in z] if isinstance(z, list) else np.real(ctm.log(z)) 

def Exp(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    try:
    #        return np.exp(z)
    #    except:
    #        return np.nan
    
    return [np.exp(a) for a in z] if isinstance(z, list) else np.exp(z) 

def Sinh(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    try:
    #        return np.sinh(z)
    #    except:
    #        return np.nan
    return [np.sinh(a) for a in z] if isinstance(z, list) else np.sinh(z) 

def Cosh(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    try:
    #        return np.cosh(z)
    #    except:
    #        return np.nan
    return [np.cosh(a) for a in z] if isinstance(z, list) else np.cosh(z) 

def Tanh(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    try:
    #        return np.tanh(z)
    #    except:
    #        return np.nan
    return [np.tanh(a) for a in z] if isinstance(z, list) else np.tanh(z) 

def Csch(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    try:
    #        return 1 / np.sinh(z)
    #    except:
    #        return np.nan
    return [1 / np.sinh(a) for a in z] if isinstance(z, list) else 1 / np.sinh(z) 

def Sech(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    try:
    #        return 1 / np.cosh(z)
    #    except:
    #        return np.nan
    return [1 / np.cosh(a) for a in z] if isinstance(z, list) else 1 / np.cosh(z)

def Coth(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    try:
    #        return np.cosh(z) / np.sinh(z)
    #    except:
    #        return np.nan
    return [np.cosh(a) / np.sinh(a) for a in z] if isinstance(z, list) else np.cosh(z) / np.sinh(z) 

def Sign(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    try:
    #        return float(np.sign(z))
    #    except:
    #        return np.nan
    return [float(np.sign(a)) for a in z] if isinstance(z, list) else float(np.sign(z))

def Cos(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, (float,int)):
    #    try:
    #        return np.cos(z)
    #    except:
    #        return np.nan
    return [np.cos(a) for a in z] if isinstance(z, list) else np.cos(z) 

def Sin(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    try:
    #        return np.sin(z)
    #    except:
    #        return np.nan
    #else:
    return [np.sin(a) for a in z] if isinstance(z, list) else np.sin(z) #if isinstance(z, complex) else np.nan 

    #return [np.sin(a) for a in z] #if isinstance(z, list) else np.sin(z) if isinstance(z, complex) else np.nan

def Tan(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    try:
    #        return np.tan(z)
    #    except:
    #        return np.nan
    return [np.tan(a) for a in z] if isinstance(z, list) else np.tan(z)

def Csc(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    try:
    #        return 1 / np.sin(z)
    #    except:
    #        return np.nan
    return [1 / np.sin(a) for a in z] if isinstance(z, list) else 1 / np.sin(z)

def Sec(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    try:
    #        return 1 / np.cos(z)
    #    except:
    #        return np.nan
    return [1 / np.cos(a) for a in z] if isinstance(z, list) else 1 / np.cos(z) 

def Cot(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    try:
    #        return np.cos(z) / np.sin(z)
    #    except:
    #        return np.nan
    return [np.cos(a) / np.sin(a) for a in z] if isinstance(z, list) else np.cos(z) / np.sin(z)

def Asin(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    try:
    #        return np.real(ctm.asin(z))
    #    except:
    #        return np.nan
    return [np.real(ctm.asin(a)) if isinstance(a, complex) else np.nan for a in z] if isinstance(z, list) else np.real(ctm.asin(z))

def Acos(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    try:
    #        return np.real(ctm.acos(z))
    #    except:
    #        return np.nan
    return [np.real(ctm.acos(a)) if isinstance(a, complex) else np.nan for a in z] if isinstance(z, list) else np.real(ctm.acos(z))

def Abs(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    return abs(z)
    return [abs(a) for a in z] if isinstance(z, list) else abs(z)

def Real(z):
    if isinstance(z, str):
        z = Transltr(z)
    #if isinstance(z, complex):
    #    return np.real(z)
    return [np.real(a) for a in z] if isinstance(z, list) else np.real(z)

def Atanr(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, complex):
        z=Real(z)
    #if isinstance(z, complex):
    #    try:
    #        return np.real(ctm.atan(z))
    #    except:
    #        return np.nan
    return [np.real(ctm.atan(a)) if isinstance(a, complex) else np.nan for a in z] if isinstance(z, list) else np.real(ctm.atan(z))

def Norm(z):
    if isinstance(z, str):
        z = Transltr(z)
    if isinstance(z, list):
        z = np.array(z)
    if isinstance(z, complex):
        try:
            z=Real(z)    
        except:
            z.all()
    #if isinstance(z, complex):
    #    return np.real(np.linalg.norm(z))
    return [float(np.linalg.norm(z)) for a in z] if isinstance(z, list) else np.linalg.norm(z)
