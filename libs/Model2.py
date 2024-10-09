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
    w1=u[17]
    w2=u[18]
    beta1=u[19]
    beta2=u[20]
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

    #K_1=[1,1]
    #K_2=[1,1]
    K_1=[1,1,1,1,1,1,1,1]
    K_2=[1,1,1,1,1,1,1,1]
    individual=str(indR1)
    try:
        vel_u=Real(eval(individual.replace('"', '').replace("'", '')))
    except ValueError:#Excepcion para controlar una mala traduccion del individo, solo por precaucion(En teoria no deberia ocurrir nunca)
        sys.exit()
    ##########################################################################
    vR1b=0.0##Real((cmath.log(np.abs(cmath.log(Cos(cmath.log(np.linalg.norm(Minus(q1,OrR1R1)))))))*cmath.log(np.linalg.norm(Minus(q1,OrR1R1)))))+Real((cmath.log(np.abs(cmath.log(Cos(cmath.log(np.linalg.norm(Minus(q2,OrR2R1)))))))*cmath.log(np.linalg.norm(Minus(q2,OrR2R1)))))
    
    #vR1b=(np.real(cmath.log(np.abs(cmath.log(cmath.cos(cmath.log(np.linalg.norm(Minus(q1,OrR1R1)))))))*cmath.log(np.linalg.norm(Minus(q1,OrR1R1)))))+(np.real(cmath.log(np.abs(cmath.log(cmath.cos(cmath.log(np.linalg.norm(Minus(q2,OrR2R1)))))))*cmath.log(np.linalg.norm(Minus(q2,OrR2R1)))))
    #############################################################################

    vR2=Plus(vel_u,vR1b)
    vR1=Plus(vel_u,vR1b)
    vel_1,w_r1=OmniModel(vR1,K_1,qd_p1,qd1,q1,beta1,w1)
    vel_2,w_r2=OmniModel(vR2,K_2,qd_p2,qd2,q2,beta2,w2)
    return vel_1,vel_2,w_r1,w_r2

def OmniModel(Vel,K,vel_des,pos_des,pos_q,beta,w):
    radio=0.040#Radio de la rueda en CM
    l_2=0.09465#Distancia del par de ruedas 1 al centro
    l_1=0.20056#Distancia del par de ruedas 2 al centro
    alpha=l_1+l_2
    
    vr1=[Times(Vel,Cos(beta)),Times(Vel,Sin(beta))]
    xd_p=vel_des[0]
    yd_p=vel_des[1]
    
    q_x=pos_q[0]
    q_y=pos_q[1]   
    
    v_x=vr1[0][0]
    v_y=vr1[1][0]
    beta_0=Atanr(q_y/q_x)
    
    x_d=pos_des[0]
    y_d=pos_des[1]
    
    Kp_1=K[0]
    Kp_2=K[1]
    Kp_3=K[2]
    Kp_4=K[3]
    Kd_1=K[4]
    Kd_2=K[5]
    Kd_3=K[6]
    Kd_4=K[7]
    
    w_1=w[0]
    w_2=w[1]
    w_3=w[2]
    w_4=w[3]
    
    #Velocidad angular del motor 1
    #alpha=w/t
    #Desplazamiento angular
    #theta = (1/2 * alpha)*(t**2)
    #Desplazamiento lineal
    #x_1=R*theta
    #Error de posición

    e=Times(1,Sqrt(Plus(Minus(y_d,q_y)**2,Minus(x_d,q_x)**2)))#Error de posición angular
    w0_1=-(v_x+v_y+(alpha)*beta_0)/radio
    w0_2=(v_x+v_y+(alpha)*beta_0)/radio
    w0_3=-(v_x+v_y+(alpha)*beta_0)/radio
    w0_4=(v_x+v_y+(alpha)*beta_0)/radio

    e_p1=[w0_1-w_1]#Error de velocidad angular
    e_p2=[w0_2-w_2]#Error de velocidad angular
    e_p3=[w0_3-w_3]#Error de velocidad angular
    e_p4=[w0_4-w_4]#Error de velocidad angular
    
    Pd_1=Plus(Kp_1*e,Kd_1*e_p1)
    Pd_2=Plus(Kp_2*e,Kd_2*e_p2)
    Pd_3=Plus(Kp_3*e,Kd_3*e_p3)
    Pd_4=Plus(Kp_4*e,Kd_4*e_p4)
    
    w_1=Times(2.07,Pd_1)#Velocidad angular del motor 1
    w_2=Times(1.955,Pd_2)#Velocidad angular del motor 2
    w_3=Times(1.486,Pd_3)#Velocidad angular del motor 3
    w_4=Times(1.686,Pd_4)#Velocidad angular del motor 4

    V_x=(radio/4)*(-w_1[0]+w_2[0]-w_3[0]+w_4[0])
    V_y=(radio/4)*(w_1[0]+w_2[0]+w_3[0]+w_4[0])
    beta=(radio/4)*((w_1[0]/(alpha))-(w_2[0]/(alpha))-(w_3[0]/(alpha))+(w_4[0]/(alpha)))
    w=[w_1[0],w_2[0],w_3[0],w_4[0]]
    Vel_R=list([V_x,V_y])
    W_r=list([[beta],w])
    return Vel_R,W_r
    