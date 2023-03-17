import numpy as np
import math as mat
import cmath as ctm
import warnings
warnings.filterwarnings("ignore")
np.seterr(all='warn')
NaN=mat.nan
Inf=mat.inf
def Minus(x,y):
    '''
    x and y take any value. 
    Minus function map x-y, then return list or float.
    '''
    fail=False
    def resta(a0,b0):#Resta de listas
        res0=a0-b0
        return res0
    if(isinstance(y,list)):#and(isinstance(x,(float,int))):
        x=x*np.ones(len(y))
    if(isinstance(x,list)):#and(isinstance(y,(float,int))):
        y=y*np.ones(len(x))
    try:
        res=map(resta,x,y)
        res=list(res)
        fail=True
    except(TypeError):
        x=Real(x)
        y=Real(y)
    finally:
        if fail==False:
            res=resta(x,y)
    return res

def Plus(x,y):
    '''
    x and y take any value. 
    Plus function map x+y, then return list or float.
    '''
    fail=False
    def suma(a1,b1):
        res1=a1+b1
        return res1
    if(isinstance(y,list)):#and(isinstance(x,(float,int))):
        x=x*np.ones(len(y))
    if(isinstance(x,list)):#and(isinstance(y,(float,int))):
        y=y*np.ones(len(x))
    try:
        res=map(suma,x,y)
        res=list(res) 
        fail=True
    except(TypeError):
        x=Real(x)
        y=Real(y)
    finally:
        if fail==False:
            res=suma(x,y)
    return res

def Times(x,y):
    '''
    x and y take any value. 
    Times function map x*y, then return list or float.
    '''
    fail=False
    def multiplicacion1D(a2,b2):
        res2=a2*b2
        return res2
    if(isinstance(y,list)):#and(isinstance(x,(float,int))):
        x=x*np.ones(len(y))
    if(isinstance(x,list)):#and(isinstance(y,(float,int))):
        y=y*np.ones(len(x))
    try:
        res=map(multiplicacion1D,x,y)
        res=list(res) 
        fail=True
    except(TypeError):
        x=Real(x)
        y=Real(y)
    finally:
        if fail==False:
            res=multiplicacion1D(x,y)                          
    return res

def Power(x,y):
    '''
    x and y take any value. 
    Power function map x^y or x**y, then return list or float.
    '''
    fail=False
    def exponente(a3,b3):
        res3=pow(a3,b3)
        return res3
    if(isinstance(y,list)):#and(isinstance(x,(float,int))):
        x=x*np.ones(len(y))
    if(isinstance(x,list)):#and(isinstance(y,(float,int))):
        y=y*np.ones(len(x))
    try:
        res=map(exponente,x,y)
        res=list(res)
        fail=True
    except(TypeError):
        x=Real(x)
        y=Real(y)
    finally:
        if fail==False:
            res=exponente(x,y)        
    return res

def Divide(x,y):
    '''
    x and y take any value. 
    Divide function map x/y with zero division restriction, then return list or float.
    '''
    fail=False
    def division(a35,b35):
        try:
            res35=a35/b35
        except ZeroDivisionError:
            res35=NaN
        return res35
    if(isinstance(y,list)):#and(isinstance(x,(float,int))):
        x=x*np.ones(len(y))
    if(isinstance(x,list)):#and(isinstance(y,(float,int))):
        y=y*np.ones(len(x))
    try:
        res=map(division,x,y)
        res=list(res)  
        fail=True
    except(TypeError):
        x=Real(x)
        y=Real(y)
    finally:
        if fail==False:
            res=division(x,y)                  
    return res

def Maximum(x,y):
    '''
    x and y take any value. 
    Maximum function map max(x,y), then return list or float.
    '''
    fail=False
    def MAXIMUM(a40,b40):
        res40=max(a40,b40)
        return res40
    if(isinstance(y,list)):
        x=x*np.ones(len(y))
    if(isinstance(x,list)):
        y=y*np.ones(len(x))
    try:
        res=map(MAXIMUM,x,y)
        res=list(res)
        fail=True
    except(TypeError):
        x=Real(x)
        y=Real(y)
    finally:
        if fail==False:
            res=MAXIMUM(x,y)
    if(isinstance(res,list)):
        res=max(res)
    return res

def Minimum(x,y):
    '''
    x and y take any value. 
    Minimum function map min(x,y), then return list or float.
    '''
    fail=False
    def MINIMUM(a41,b41):
        res41=min(a41,b41)
        return res41
    if(isinstance(y,list)):
        x=x*np.ones(len(y))
    if(isinstance(x,list)):
        y=y*np.ones(len(x))
    try:
        res=map(MINIMUM,x,y)
        res=list(res)
        fail=True
    except(TypeError):
        x=Real(x)
        y=Real(y)
    finally:
        if fail==False:
            res=MINIMUM(x,y)
    if(isinstance(res,list)):
        res=min(res)
    return res

def Atan2r(x,y):
    '''
    x and y take any value, then return a list or float
    '''
    fail=False
    def arcotangente2(a42,b42):
        try:
            res42=np.arctan2(np.real(a42),np.real(b42))
        except:
            res42=NaN
        return res42
    if(isinstance(y,list)):
        x=x*np.ones(len(y))
    if(isinstance(x,list)):
        y=y*np.ones(len(x))    
    try:
        res=map(arcotangente2,x,y)
        res=list(res)  
        fail=True
    except(TypeError):
        x=Real(x)
        y=Real(y)   
    finally:
        if fail==False:  
            res=arcotangente2(x,y)
    return res

def Sqrt(z):
    '''
    @param z takes any value, then return list or float
    '''
    def raiz(a):
        res22=np.sqrt(a)
        return res22
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=raiz(z)
    except:
        res=map(raiz,z)
        res=list(res)
    return res

def Sqr(z):
    '''
    @param z takes any value, then return list or float
    '''
    def exponente2(a):
        res21=pow(a,2)
        return res21
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=exponente2(z)
    except:
        res=map(exponente2,z)
        res=list(res)
    return res

def Logn(z):
    '''
    @param z takes any value, then return list or float
    '''
    def logaritmo(a):
        try:
            res20=np.real(ctm.log(a))
        except:
            res20=NaN
        return res20
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=logaritmo(z)
    except:
        res=map(logaritmo,z)
        res=list(res)        
    return res

def Exp(z):
    '''
    @param z takes any value, then return list or float
    '''
    def exponencial(a):
        try:
            res19=np.exp(a)
        except:
            res19=NaN
        return res19
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=exponencial(z)
    except:
        res=map(exponencial,z)
        res=list(res)
    return res

def Sinh(z):
    '''
    @param z takes any value, then return list or float
    '''
    def senohyperbolico(a):
        try:
            res18=np.sinh(a)
        except:
            res18=NaN
        return res18
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=senohyperbolico(z)
    except:
        res=map(senohyperbolico,z)
        res=list(res)
    return res

def Cosh(z):
    '''
    @param z takes any value, then return list or float
    '''
    def cosenohyperbolico(z):
        try:
            res17=np.cosh(z)
        except:
            res17=NaN
        return res17
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=cosenohyperbolico(z)
    except:
        res=map(cosenohyperbolico,z)
        res=list(res)
    return res
def Tanh(z):
    '''
    @param z takes any value, then return list or float
    '''
    def tangentehyperbolica(z):
        try:
            res16=np.tanh(z)
        except:
            res16=NaN
        return res16
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=tangentehyperbolica(z)
    except:
        res=map(tangentehyperbolica,z)
        res=list(res)
    return res
def Csch(z):
    '''
    @param z takes any value, then return list or float
    '''
    def cosecantehyperbolica(z):
        try:
            res15=1/np.sinh(z)
        except:
            res15=NaN
        return res15
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=cosecantehyperbolica(z)
    except:
        res=map(cosecantehyperbolica,z)
        res=list(res)
    return res
def Sech(z):
    '''
    @param z takes any value, then return list or float
    '''
    def secantehyperbolica(z):
        try:
            res14=1/np.cosh(z)
        except:
            res14=NaN
        return res14
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=secantehyperbolica(z)
    except:
        res=map(secantehyperbolica,z)
        res=list(res)
    return res
def Coth(z):
    '''
    @param z takes any value, then return list or float
    '''
    def cotangentehyperbolica(z):
        try:
            res13=np.cosh(z)/np.sinh(z)
        except:
            res13=NaN
        return res13
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=cotangentehyperbolica(z)
    except:
        res=map(cotangentehyperbolica,z)
        res=list(res)
    return res
  
def Sign(z):
    '''
    @param z takes any value, then return list or float
    '''  
    def signo(z):
        try:
            res12=np.sign(z)
        except:
            res12=NaN
        return float(res12)
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=signo(z)
    except:
        res=map(signo,z)
        res=list(res)
    return res
'''
    @param z takes any value, then return list or float
'''
def Cos(z):
    def coseno(z):
        try:
            res11=np.cos(z)
        except:
            res11=NaN
        return res11
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=coseno(z)
    except:
        res=map(coseno,z)
        res=list(res)
    return res
'''
    @param z takes any value, then return list or float
'''
def Sin(z):
    def sinusoidal(z):
        try:
            res10=np.sin(z)
        except:
            res10=NaN
        return res10
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=sinusoidal(z)    
    except:
        res=map(sinusoidal,z)
        res=list(res)
    return res
'''
    @param z takes any value, then return list or float
'''
def Tan(z):
    def tangente(z):
        try:
            res9=np.tan(z)
        except:
            res9=NaN
        return res9
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=tangente(z)
    except:
        res=map(tangente,z)
        res=list(res)
    return res
'''
    @param z takes any value, then return list or float
'''
def Csc(z):
    def cosecante(z):
        try:
            res8=1/np.sin(z)
        except:
            res8=NaN
        return res8
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=cosecante(z)
    except:
        res=map(cosecante,z)
        res=list(res)
    return res
'''
    @param z takes any value, then return list or float
'''
def Sec(z):
    def secante(z):
        try:
            res7=1/np.cos(z)
        except:
            res7=NaN
        return res7
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=secante(z)
    except:
        res=map(secante,z)
        res=list(res)
    return res
'''
    @param z takes any value, then return list or float
'''
def Cot(z):
    def cotangente(z):
        try:
            res6=np.cos(z)/np.sin(z)
        except:
            res6=NaN
        return res6
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=cotangente(z)
    except:
        res=map(cotangente,z)
        res=list(res)
    return res
'''
    @param z takes any value, then return list or float
'''
def Asin(z):
    def arcosin(z):
        try:
            res5=np.real(ctm.asin(z))
        except:
            res5=NaN
        return res5
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=arcosin(z)
    except:
        res=map(arcosin,z)
        res=list(res)
    return res
'''
    @param z takes any value, then return list or float
'''    
def Acos(z):
    def arcocoseno(z):
        try:
            res4=np.real(ctm.acos(z))
        except:
            res4=NaN
        return res4
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=arcocoseno(z)
    except:
        res=map(arcocoseno,z)
        res=list(res)
    return res
'''
    @param z takes any value, then return list or float
'''
def Abs(z):
    def absoluto(z):
        res3=abs(z)
        return res3
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=absoluto(z)
    except:
        res=map(absoluto,z)
        res=list(res)
    return res
'''
    @param z takes any value, then return list or float
'''
def Real(z):
    def real(z):
        if ((isinstance(z,float)or isinstance(z,int) or isinstance(z,np.float64))):
            res2=np.real(z)
        else:
            res2=np.real(z.all())
        return res2
    try:
        res=real(z)
    except:
        res=map(real,z)
        res=list(res)
    return res
'''
    @param z takes any value, then return list or float
'''
def Atanr(z):
    def Arcotanr(z):
        try:
                res1=np.real(ctm.atan(z))
        except:
                res1=NaN
        return res1
    if (isinstance(z,complex)):
        z=Real(z)
    try:
        res=Arcotanr(z)
    except:
        res=map(Arcotanr,z)
        res=list(res)
    return res
'''
    @param z takes any value, then return list or float
'''
def Norm(z):
    def norma(z):
        res0=np.real(np.linalg.norm(z))
        return res0
    try:
        res=norma(z)
    except:
        res=norma(z.tolist())
    return res
