import sys
sys.path.insert(0, '~/libs')
sys.path.insert(1, '~/Simulation')
from libs.Math import Plus, Minus, Divide, Times,Power, Maximum, Minimum, Atan2r
from libs.Math import Sqrt, Sqr, Logn, Exp, Sinh, Cosh, Tanh, Csch, Sech, Coth, Cos, Sin, Tan, Csc, Sec, Cot, Asin, Acos, Norm, Abs, Real, Atanr
import numpy as np
from math import nan as NaN
from math import inf as Inf
import cmath

def IndividualTest(u,indR1,r,u0):
    r1=r[0]#Radio del robot 1
    r2=r[1]#Radio del robot 2
    rRb1=r1+r2#Consideración de ambos radios
    q1=[u[0],u[1]]#Posicion del robo 1
    q2=[u[2],u[3]]#Posicion del robot x
    qx2=q2[0]#Posicion en X del robot 2 
    qy2=q2[1]#Posicion en y del robot 2
    qx1=q1[0]#Posicion en x del robot 1
    qy1=q1[1]#Posicion en y del robot 1
    xd1=u[4][0]#Posicion deseada del robot 1 en x
    xdp1=u[10]#Componente de Velocidad deseada del robot 1 en x
    yd1=u[4][1]#Posicion deseada del robot 1 en y
    ydp1=u[11]#Componente de Velocidad deseada del robot 1 en y
    xd2=u[5][0]
    xdp2=u[12] 
    yd2=u[5][1] 
    ydp2=u[13]
    Vx1=u[6]
    Vy1=u[7]
    Vx2=u[8]
    Vy2=u[9]
    qd_p1=[xdp1,ydp1]
    qd_p2=[xdp2,ydp2]
    qd1=[xd1,yd1]
    qd2=[xd2,yd2]
    V1=[Vx1,Vy1]
    V2=[Vx2,Vy2]
    t1=u[14]
    t2=u[15]
    tR=[t1,t2]
    td=u[16]
    tdR=[td,td]
        
    OrR2R1=Plus(q1,Divide(Times(rRb1,Minus(q2,q1)),Norm(Minus(q2,q1))))
    OrR1R1=Plus(q2,Divide(Times(rRb1,Minus(q1,q2)),Norm(Minus(q1,q2))))

    K_1=[1,1]
    K_2=[1,1]
    individual=str(indR1)
    try:
        vel_u=eval(individual.replace('"', '').replace("'", ''))
    except ValueError:#Excepcion para controlar una mala traduccion del individo, solo por precaucion(En teoria no deberia ocurrir nunca)
        sys.exit()
    ##########################################################################
    vR1b=((cmath.log(np.abs(cmath.log(Cos(cmath.log(np.linalg.norm(Minus(q1,OrR1R1)))))))*cmath.log(np.linalg.norm(Minus(q1,OrR1R1)))))+((cmath.log(np.abs(cmath.log(Cos(cmath.log(np.linalg.norm(Minus(q2,OrR2R1)))))))*cmath.log(np.linalg.norm(Minus(q2,OrR2R1)))))
    
    #vR1b=(np.real(cmath.log(np.abs(cmath.log(cmath.cos(cmath.log(np.linalg.norm(Minus(q1,OrR1R1)))))))*cmath.log(np.linalg.norm(Minus(q1,OrR1R1)))))+(np.real(cmath.log(np.abs(cmath.log(cmath.cos(cmath.log(np.linalg.norm(Minus(q2,OrR2R1)))))))*cmath.log(np.linalg.norm(Minus(q2,OrR2R1)))))
    #############################################################################

    vR2=Plus(vel_u,vR1b)
    vR1=Plus(vel_u,vR1b)
    vel_1=[ModelOfRobot(vR1,K_1,qd_p1,qd1,q1)]
    vel_2=[ModelOfRobot(vR2,K_2,qd_p2,qd2,q2)]
    return vel_1,vel_2

def ModelOfRobot(Vel_u,K,vel_des,pos_des,pos_q):
    xd_p=vel_des[0]
    yd_p=vel_des[1]
    x_d=pos_des[0]
    y_d=pos_des[1]
    q_x=pos_q[0]
    q_y=pos_q[1]
    k_1=K[0]
    k_2=K[1]
    VxR_a=xd_p+k_1*(x_d-q_x)
    VyR_b=yd_p+k_2*(y_d-q_y)
    if (~isinstance(Vel_u,(float,np.float64)))>1:
        Vx_u=Vel_u[0]
        Vy_u=Vel_u[1]
        VxR_r=Times(Vx_u,(y_d-q_y))
        VyR_r=Times(Times(-1,Vy_u),(x_d-q_x))
    else:
        VxR_r=Times(Vel_u,(y_d-q_y))
        VyR_r=Times(Times(-1,Vel_u),(x_d-q_x))

    vxR1=Plus(VxR_a,VxR_r)
    vyR1=Plus(VyR_b,VyR_r)
    Vel_R=list([vxR1,vyR1])
    return Vel_R
