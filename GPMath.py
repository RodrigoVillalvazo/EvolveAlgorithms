import numpy as np
import math as mat
import cmath as ctm
#import sys
#import pickle
#nan=mt.nan
#inf=mt.inf
NaN=mat.nan
Inf=mat.inf
def Minus(x,y):
        def resta(a0,b0):#Resta de listas
                res0=a0-b0
                return res0
        if(isinstance(x,str))or(isinstance(y,str)):
                res='list(map(resta,'+str(x)+','+str(y)+'))'
        elif(isinstance(x,list))and(isinstance(y,list)):
                res=list(map(resta,x,y))
        elif(isinstance(x,float))and(isinstance(y,float)):
                res=resta(x,y)
        elif(isinstance(x,int))and(isinstance(y,int)):
                res=resta(x,y)
        else:
                res=NaN
        return res
def Plus(x,y):
        def suma(a1,b1):
                res1=a1+b1
                return res1
        if(isinstance(x,str))or(isinstance(y,str)):
                res='list(map(suma,'+str(x)+','+str(y)+'))'
        elif(isinstance(x,list))and(isinstance(y,list)):
                res=list(map(suma,x,y))
        elif(isinstance(x,float))and(isinstance(y,float)):
                res=suma(x,y)
        elif(isinstance(x,int))and(isinstance(y,int)):
                res=suma(x,y)
        else:
                res=NaN
        return res

def Times(x,y):
        def multiplicacion1D(a2,b2):
                res2=a2*b2
                return res2
        if(isinstance(x,str))or(isinstance(y,str)):
                res='list(map(suma,'+str(x)+','+str(y)+'))'
        elif(isinstance(x,list))and((isinstance(y,float)or(isinstance(y,int)))):        
                res=list(map(multiplicacion1D,x,y+np.zeros(len(x))))
        elif(isinstance(y,list))and((isinstance(x,float)or(isinstance(x,int)))):        
                res=list(map(multiplicacion1D,x+np.zeros(len(y)),y))
        elif(isinstance(x,float))and(isinstance(y,float)):
                res=multiplicacion1D(x,y)
        elif(isinstance(x,int))and(isinstance(y,int)):
                res=multiplicacion1D(x,y)
        else:
                res=NaN
        return res
def Power(x,y):
        def exponente(a3,b3):
                try:
                        res3=pow(a3,b3)
                except(ZeroDivisionError,OverflowError):
                        res3=NaN
                return res3
        if(isinstance(x,str))or(isinstance(y,str)):
                res='list(map(exponente,'+str(x)+','+str(y)+'))'
        else:
                res=list(map(exponente,x,y))
        return res
def Divide(x,y):
        def division(a35,b35):
                try:
                        res35=a35/b35
                except ZeroDivisionError:
                        res35=NaN
                return res35
        if(isinstance(x,float))and(isinstance(y,float)):
                res=division(x,y)
        elif(isinstance(x,int))and(isinstance(y,int)):
                res=division(x,y)
        elif(isinstance(x,list))and((isinstance(y,float)or(isinstance(y,int)))):        
                res=list(map(division,x,(1/y)+np.zeros(len(x))))
        elif(isinstance(y,list))and((isinstance(x,float)or(isinstance(x,int)))):        
                res=list(map(division,(1/x)+np.zeros(len(y)),y))
        else:
                res=NaN                
        return res
def maximum(x,y):
        if(isinstance(x,list)==True)and(isinstance(y,float)==True):
                x=max(np.real(x))
        elif(isinstance(x,float)==True)and(isinstance(y,list)==True):
                y=max(np.real(y))
        elif(isinstance(x,list)==True)and(isinstance(y,list)==True):
                x=max(np.real(x))
                y=max(np.real(y))
        try:
                res=map(max,x,y)
        except:
                res=max(x,y)                
        return res
def minimum(x,y):
        if(isinstance(x,list)==True)and(isinstance(y,float)==True):
                x=min(np.real(x))
        elif(isinstance(x,float)==True)and(isinstance(y,list)==True):
                y=min(np.real(y))
        elif(isinstance(x,list)==True)and(isinstance(y,list)==True):
                x=min(np.real(x))
                y=min(np.real(y))
        try:
                res=map(min,x,y)
        except:
                res=min(x,y)
        return res
def atan2r(x,y):
        res=np.real(mat.atan2(x,y))
        return res
def sqrt(z):
        if(isinstance(z,str)):
                try:
                        res='ctm.sqrt('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=ctm.sqrt(z)
                except:
                        res=NaN
        return res
def sqr(z):
        if(isinstance(z,str)):
                try:
                        res='pow('+str(z)+','+str(2)+')'
                except:
                        res=NaN
        else:
                try:
                        res=pow(z,2)
                except:
                        res=NaN
        return res
def Log(z):
        if(isinstance(z,str)):
                try:
                        res='ctm.log('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=ctm.log(z)
                except:
                        res=NaN
        return res
def exp(z):
        if(isinstance(z,str)):
                try:
                        res='ctm.exp('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=ctm.exp(z)
                except:
                        res=NaN
        return res
def sinh(z):
        if(isinstance(z,str)):
                try:
                        res='ctm.sinh('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=ctm.sinh(z)
                except:
                        res=NaN
        return res
def cosh(z):
        if(isinstance(z,str)):
                try:
                        res='ctm.cosh('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=ctm.cosh(z)
                except:
                        res=NaN
        return res
def tanh(z):
        if(isinstance(z,str)):
                try:
                        res='ctm.tanh('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=ctm.tanh(z)
                except:
                        res=NaN
        return res
def csch(z):
        if(isinstance(z,str)):
                try:
                        res='1/ctm.sinh('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=1/ctm.sinh(z)
                except:
                        res=NaN
        return res
def sech(z):
        if(isinstance(z,str)):
                try:
                        res='1/ctm.cosh('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=1/ctm.cosh(z)
                except:
                        res=NaN
        return res

def coth(z):
        if(isinstance(z,str)):
                try:
                        res='ctm.cosh('+str(z)+')/'+'ctm.sinh('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=ctm.cosh(z)/ctm.sinh(z)
                except:
                        res=NaN
        return res
def sign(z):
        if(isinstance(z,str)):
                try:
                        res='np.sign('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=np.sign(z)
                except:
                        res=NaN
        return res

def cos(z):
        if(isinstance(z,str)):
                try:
                        res='ctm.cos('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=ctm.cos(z)
                except:
                        res=NaN
        return res
def sin(z):
        if(isinstance(z,str)):
                try:
                        res='ctm.sin('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=ctm.sin(z)
                except:
                        res=NaN
        return res
def tan(z):
        if(isinstance(z,str)):
                try:
                        res='ctm.tan('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=ctm.tan(z)
                except:
                        res=NaN
        return res
def csc(z):
        if(isinstance(z,str)):
                try:
                        res='1/ctm.sin('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=1/ctm.sin(z)
                except:
                        res=NaN
        return res
def sec(z):
        if(isinstance(z,str)):
                try:
                        res='1/ctm.cos('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=1/ctm.cos(z)
                except:
                        res=NaN
        return res
def cot(z):
        if(isinstance(z,str)):
                try:
                        res='ctm.cos('+str(z)+')/'+'ctm.sin('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=ctm.cos(z)/ctm.sin(z)
                except:
                        res=NaN
        return res
def asin(z):
        if(isinstance(z,str)):
                try:
                        res='ctm.asin('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=ctm.asin(z)
                except:
                        res=NaN
        return res
def acos(z):
        if(isinstance(z,str)):
                try:
                        res='ctm.acos('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=ctm.acos(z)
                except:
                        res=NaN
        return res
def Abs(z):
        if(len(z)>1)and(isinstance(z,list)==True):
                z1=np.linalg.norm(z[0])
                z2=np.linalg.norm(z[1])
                res=[abs(z1),abs(z2)]
        else:
                res=abs(z)
        return res
def real(z):
        if(isinstance(z,str)):
                try:
                        res='np.real('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=np.real(z)
                except:
                        res=NaN
        return res
##Funcion ArcoTangenteReal##
def atanr(z):
        if(isinstance(z,str)):
                try:
                        res='np.real(ctm.atan('+str(z)+'))'
                except:
                        res=NaN
        else:
                try:
                        res=np.real(ctm.atan(z))
                except:
                        res=NaN
        return res
##Funcion Norma##
#         Forma simple de llamar la norma euclidiana
def norm(z):
        if(isinstance(z,str)):
                try:
                        res='np.linalg.norm('+str(z)+')'
                except:
                        res=NaN
        else:
                try:
                        res=np.linalg.norm(z)
                except:
                        res=NaN
        return res.tolist()
