# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 19:12:42 2025

@author: serdg
"""
import cmath
from math import inf
from libs.Math import Plus, Minus, Divide, Times,Power, Maximum, Minimum, Atan2r
from libs.Math import Sqrt, Sqr, Logn, Exp, Sinh, Cosh, Tanh, Csch, Sech, Coth, Cos, Sin, Tan, Csc, Sec, Cot, Asin, Acos, Norm, Abs, Real, Atanr
import numpy as np
import sys
saturacion=inf#Velocidad maxima
def Simulacion(ind=None,pos=0.0,pd=0.0,r=0.10,tf=100000,td=1000,dt=0.001,ep=0.0001):
    """
    [Struct] ind - Individuo a evaluar \n
    [List] pos - Vector de posicion de los robots \n
    [List] pd - Vector de posicion deseada \n
    [List] r - Vector de radios de los robots \n
    [Int] tf - tiempo de simulacion \n
    [int] td - tiempo deseado \n
    [int] dt - Paso de integracion \n
    [int] ep - Epsilon para evitar indefiniciones \n
    """
    Try1=[]
    Try2=[]
    Try3=[]
    Try4=[]
    ds1=[]
    ds2=[]
    ts1=[]
    ts2=[]
    do1=[]
    do2=[]
    Vx1=[]
    Vy1=[]
    Vx2=[]
    Vy2=[]
    tR1saved=0.0
    tR2saved=0.0
    r1=r[0]
    r2=r[1]
    aux1=1
    aux2=1
    z=1
    #Obtener velocidades
    radio=(r1+r2)+ep
    #Posicion del obstaculo
    x_1=float(eval(str(pos[0][0]).replace('"', '').replace("'", '')))#float
    y_1=float(eval(str(pos[0][1]).replace('"', '').replace("'", '')))#float
    x_2=float(eval(str(pos[1][0]).replace('"', '').replace("'", '')))#float
    y_2=float(eval(str(pos[1][1]).replace('"', '').replace("'", '')))#float
    xd_1=float(pd[0][0])
    yd_1=float(pd[0][1])
    xd_2=float(pd[1][0])
    yd_2=float(pd[1][1])
    xd_p1=0.0
    yd_p1=0.0
    xd_p2=0.0
    yd_p2=0.0
    
    Vx_1=0.0
    Vy_1=0.0
    Vx_2=0.0
    Vy_2=0.0

    t_1=0.0
    t_2=0.0

    #distancia inicial del robot al objetivo
    q_1=[x_1,y_1]
    q_2=[x_2,y_2]
    qd_1=[xd_1,yd_1]
    qd_2=[xd_2,yd_2]
    
    do_1=np.linalg.norm(Minus(q_1,qd_1))#Distancia al objetivo 1
    do_2=np.linalg.norm(Minus(q_2,qd_2))#Distancia al objetivo 2
    dr_1=do_1#Distancia del robot 1 a la meta
    dr_2=do_2#Distancia del robot 1 a la meta
    ds_1=np.linalg.norm(Minus(q_1,q_2))#Distancia al obstaculo 1
    ds_2=np.linalg.norm(Minus(q_2,q_1))#Distancia al obstaculo 2


    #vR2c=str(ind).replace('"', '').replace("'", '')
###############################################################################    
    OrR1R1=distancia_entre_robots(r=radio, q_a=q_1, q_b=q_2)
    OrR1R1x,OrR1R1y=[OrR1R1[0],OrR1R1[1]]
    OrR2R1=distancia_entre_robots(r=radio, q_a=q_2, q_b=q_1)
    OrR2R1x,OrR2R1y=[OrR2R1[0],OrR2R1[1]]
    
    try:
        vR2a=np.real(eval(str(ind)))
        pass
    except (OverflowError,MemoryError):#Excepcion para evitar operaciones con complejos y no complejos, y problemas de indeterminacion entre funciones que algun valor no este entre su dominio
        print(ind)
        print("\nSimulacion terminada por maximo de memoria consumido\n")
        sys.exit()
        pass

    vR2b=repulsor(q_A=q_1,O_rA=OrR1R1)+repulsor(q_A=q_2,O_rA=OrR2R1)   
    v=vR2a+vR2b
    Robot1=Omnidireccional(u=v,x=x_1,y=y_1,xd=xd_1,yd=yd_1,xd_p=xd_p1,yd_p=yd_p1)
    Robot2=Omnidireccional(u=v,x=x_2,y=y_2,xd=xd_2,yd=yd_2,xd_p=xd_p2,yd_p=yd_p2)    
    Vx_1,Vy_1=Robot1
    Vx_2,Vy_2=Robot2
###############################################################################
    vR1=[Robot1]
    vR2=[Robot2]

    qR1=[q_1]
    qR2=[q_2]
     
    while (t_1<=tf)and(t_2<=tf)and(ds_1>radio)and(ds_2>radio):
        
        qR1.insert(z,Plus(Times(dt,vR1[z-1]),qR1[z-1]))#actualizar posiciones del Robot 1
        qR2.insert(z,Plus(Times(dt,vR2[z-1]),qR2[z-1]))


        do_1=do_1+np.linalg.norm(Minus(qR1[z],qd_1))#distancia recorrida
        do_2=do_2+np.linalg.norm(Minus(qR2[z],qd_2))
        dr_1=np.linalg.norm(Minus(qR1[z],qd_1))
        dr_2=np.linalg.norm(Minus(qR2[z],qd_2))

        #Robot 1
        x_1=qR1[z][0]
        y_1=qR1[z][1]

        #Robot2
        x_2=qR2[z][0]
        y_2=qR2[z][1]

        
        ds_1=np.linalg.norm(Minus(qR1[z],qR2[z]))
        ds_2=np.linalg.norm(Minus(qR2[z],qR1[z]))
###############################################################################
        OrR1R1=distancia_entre_robots(r=radio, q_a=qR1[z], q_b=qR2[z])
        OrR1R1x,OrR1R1y=[OrR1R1[0],OrR1R1[1]]
        OrR2R1=distancia_entre_robots(r=radio, q_a=qR2[z], q_b=qR1[z])
        OrR2R1x,OrR2R1y=[OrR2R1[0],OrR2R1[1]]
        
        try:
            vR2a=np.real(eval(str(ind)))
            pass
        except (OverflowError,MemoryError):#Excepcion para evitar operaciones con complejos y no complejos, y problemas de indeterminacion entre funciones que algun valor no este entre su dominio
            print(ind)
            print("\nSimulacion terminada por maximo de memoria consumido\n")
            sys.exit()
            pass
        
        vR2b=repulsor(q_A=q_1,O_rA=OrR1R1)+repulsor(q_A=q_2,O_rA=OrR2R1)   
        v=vR2a+vR2b
        Robot1=Omnidireccional(u=v,x=x_1,y=y_1,xd=xd_1,yd=yd_1,xd_p=xd_p1,yd_p=yd_p1)
        Robot2=Omnidireccional(u=v,x=x_2,y=y_2,xd=xd_2,yd=yd_2,xd_p=xd_p2,yd_p=yd_p2)    
        vR1.insert(z,Robot1)
        vR2.insert(z,Robot2)
###############################################################################
        Vx_1,Vy_1=Robot1
        Vx_2,Vy_2=Robot2

        ts1.insert(z,t_1)
        ts2.insert(z,t_2)

        Try1.insert(z,qR1[z-1][0])#s.try
        Try2.insert(z,qR1[z-1][1])
        
        Try3.insert(z,qR2[z-1][0])
        Try4.insert(z,qR2[z-1][1])
        
        
        ds1.insert(z,ds_1)
        ds2.insert(z,ds_2)

        do1.insert(z,do_1)
        do2.insert(z,do_2)
        
        Vx1.insert(z,Vx_1)
        Vx2.insert(z,Vx_2)
        Vy1.insert(z,Vy_1)
        Vy2.insert(z,Vy_2)
        #Seccion de banderas
        z=z+1
        if(dr_1<0.02)and((Vx_1<0.001)and(Vy_1<0.001)and(aux1==1)):
            aux1=2
            tR1saved=t_1
        if(dr_2<0.02)and((Vx_2<0.001)and(Vy_2<0.001)and(aux2==1)):
            aux2=2
            tR2saved=t_2
        t_1=t_1+dt
        t_2=t_2+dt
    return [tR1saved,tR2saved,Try1,Try2,Try3,Try4,Vx1,Vy1,Vx2,Vy2,do1,do2,ds1,ds2,ts1,ts2]



def Omnidireccional(u=None,x=0.0,y=0.0,xd=0.0,yd=0.0,xd_p=0.0,yd_p=0.0,k1=1.0,k2=1.0,saturacion=inf):
    '''
    Creamos la función contenedora del movimiento del robot omnidireccional \n
    k1 - Ganancia 1 \n
    k2 - Ganancia 2 \n
    x - Posicion en x del robot n \n
    y - Posicion en y del robot n \n
    xd - Posicion deseada en x del robot n \n
    yd - Posicion deseada en y del robot n \n
    xd_p - Velocidad deseada en la componente x \n
    yd_p - Velocidad deseada en la componente y \n
    u - entrada de control \n
    saturacion - velocidad maxima en m/s
    regresa una tupla
    '''    
    vx_a=xd_p+k1*(xd-x)
    vx_r=u*(yd-y)
    v_x=vx_a+vx_r
    vy_a=yd_p+k2*(yd-y)
    vy_r=-u*(xd-x);
    v_y=vy_a+vy_r;
    if (v_x>saturacion):
       v_x=saturacion
       pass
    if (v_x<-saturacion):
       v_x=-saturacion
       pass
    if (v_y>saturacion):
        v_y=saturacion
        pass
    if (v_y<-saturacion): 
        v_y=-saturacion 
        pass    
    return [v_x, v_y]
def distancia_entre_robots(r=0.10,q_a=None,q_b=None):
    """
    [float] r - radio del robot  \n
    [list] q_a - vector posicion del robot A \n
    [list] q_b - vector posicion del robot B \n
    regresa una lista
    """
    return Plus(q_a,(Times(r,Minus(q_a,q_b))/np.linalg.norm(Minus(q_a,q_b))))
def repulsor(q_A=None, O_rA=None):
    """
    [List] q_A - vector posicion del robot n \n
    [List] O_rA - vector distancia del robot n contra robot n+1 \n
    regresa una lista
    """
    return np.real(cmath.log(np.abs(cmath.log(cmath.cos(cmath.log(np.linalg.norm(Minus(q_A,O_rA)))))))*cmath.log(np.linalg.norm(Minus(q_A,O_rA))))