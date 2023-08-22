from Importer import *
#Modelo del Robot #1
def ModelKaF1TestRobot1(u,indR1,r,u0):
   AF=[0]
   TF=[0]
   ZF=[0]
   OF=[0]
   EF=[0]
   zeroflag=0
   TypeFlag=0
   OverFlag=0
   ErrorFlag=0#Auxiliar para controlar errores
   r1=r[0]#Radio del robot 1
   r2=r[1]#Radio del robot 2
   rRb1=r1+r2
   q1=[u[0],u[1]]
   q2=[u[2],u[3]]

   qx2=q2[0]
   qy2=q2[1]
   qx1=q1[0]
   qy1=q1[1]

   xd1=u[4][0]
   xdp1=u[10] 
   yd1=u[4][1] 
   ydp1=u[11]

   xd2=u[5][0]
   xdp2=u[12] 
   yd2=u[5][1] 
   ydp2=u[13]


   Vx1=u[6]
   Vy1=u[7]
   Vx2=u[8]
   Vy2=u[9]
   
   qd1=[xd1,yd1]
   qd2=[xd2,yd2]
   V1=[Vx1,Vy1]
   V2=[Vx2,Vy2]
   
   t1=u[14]
   t2=u[15]
   tR=[t1,t2]
   td=u[16]
   tdR=[td,td]
   try:
       OrR1R1=Plus(q2,Divide(Times(rRb1,Minus(q1,q2)),Norm(Minus(q1,q2))))
   except (ZeroDivisionError,FloatingPointError):#Excepcion para evitar que el programa se detenga en caso de que ocurra division por cero
       OrR1R1=[NaN,NaN]
       zeroflag=1
   try:
       OrR2R1=Plus(q1,Divide(Times(rRb1,Minus(q2,q1)),Norm(Minus(q2,q1))))
   except (ZeroDivisionError,FloatingPointError):#Excepcion para evitar que el programa se detenga en caso de que ocurra division por cero
       OrR2R1=[NaN,NaN]
       zeroflag=1


   k1R1=1
   k2R1=1
   vR1c=float()
   individual=str(indR1)
   try:
       vR1c=eval(individual.replace('"', '').replace("'", ''))
   except ValueError:#Excepcion para controlar una mala traduccion del individo, solo por precaucion(En teoria no deberia ocurrir nunca)
       ErrorFlag=1
   ##########################################################################
   try:
       vR1a=np.real(vR1c)
       pass
   except ValueError:
       vR1a=NaN
       ErrorFlag=1
       pass
   except ZeroDivisionError:
       vR1a=NaN
       zeroflag=1
       pass
   except OverflowError:#Excepcion para penalizar que al momento de evaluar el individuo ocurra: division por cero, o algun error por sobreflujo(valor enorme en extremo)
       vR1a=math.inf
       OverFlag=1
       pass
   except (TypeError,MemoryError):#Excepcion para evitar operaciones con complejos y no complejos, y problemas de indeterminacion entre funciones que algun valor no este entre su dominio
       print(vR1c)
       print("\nSimulacion terminada por maximo de memoria consumido\n")
       sys.exit()
   try:
       vR1b=(np.real(cmath.log(np.abs(cmath.log(cmath.cos(cmath.log(np.linalg.norm(Minus(q1,OrR1R1)))))))*cmath.log(np.linalg.norm(Minus(q1,OrR1R1)))))+(np.real(cmath.log(np.abs(cmath.log(cmath.cos(cmath.log(np.linalg.norm(Minus(q2,OrR2R1)))))))*cmath.log(np.linalg.norm(Minus(q2,OrR2R1)))))
   except ValueError:#Excepcion para controlar una indefinicion de las funciones, solo por precaucion(En teoria no deberia ocurrir nunca)
       vR1b=NaN
       ErrorFlag=1
   vR1=Plus(vR1a,vR1b)
   vxaR1=xdp1+k1R1*(xd1-q1[0])
   if len([vR1])>1:
    vxrR1=Times(vR1[0],(yd1-q1[1]))
   else:
    vxrR1=Times(vR1,(yd1-q1[1]))
   vxR1=Plus(vxaR1,vxrR1)
   vyaR1=ydp1+k2R1*(yd1-q1[1])
   if len([vR1])>1:
    vyrR1=Times(Times(-1,vR1[1]),(xd1-q1[0]))
   else:
    vyrR1=Times(Times(-1,vR1),(xd1-q1[0]))
   vyR1=Plus(vyaR1,vyrR1)
   FlagsR1=[zeroflag,ErrorFlag,OverFlag,TypeFlag]
   cmt=1
   resR1=list(Real([vxR1,vyR1]))
   return FlagsR1 ,resR1


def ModelKaF1TestRobot2(u,indR2,r,u0):
   auxflag=1
   AF=[0]
   TF=[0]
   ZF=[0]
   OF=[0]
   EF=[0]
   zeroflag=0
   TypeFlag=0
   OverFlag=0
   ErrorFlag=0#Auxiliar para controlar errores
   r1=r[0]
   r2=r[1]
   rRb2=r1+r2
   q1=[u[0],u[1]]
   q2=[u[2],u[3]]

   qx1=q1[0]
   qy1=q1[1]
   qx2=q2[0]
   qy2=q2[1]

   xd1=u[4][0]
   xdp1=u[10] 
   yd1=u[4][1] 
   ydp1=u[11]
   xd2=u[5][0]
   xdp2=u[12] 
   yd2=u[5][1] 
   ydp2=u[13]


   Vx1=u[6]
   Vy1=u[7]
   Vx2=u[8]
   Vy2=u[9]
   
   qd1=[xd1,yd1]
   qd2=[xd2,yd2]
   V1=[Vx1,Vy1]
   V2=[Vx2,Vy2]
   
   t1=u[14]
   t2=u[15]
   tR=[t1,t2]
   td=u[16]
   tdR=[td,td]
   try:
       OrR1R1=Plus(q2,Divide(Times(rRb2,Minus(q1,q2)),Norm(Minus(q1,q2))))
   except (ZeroDivisionError,FloatingPointError):#Excepcion para evitar que el programa se detenga en caso de que ocurra division por cero
       OrR1R1=[NaN,NaN]
       zeroflag=1
   try:
       OrR2R1=Plus(q1,Divide(Times(rRb2,Minus(q2,q1)),Norm(Minus(q2,q1))))
   except (ZeroDivisionError,FloatingPointError):#Excepcion para evitar que el programa se detenga en caso de que ocurra division por cero
       OrR2R1=[NaN,NaN]
       zeroflag=1
   
   k1R2=1
   k2R2=1
   vR2c=float()
   individual=str(indR2)
   try:
       vR2c=eval(individual.replace('"', '').replace("'", ''))
   except ValueError:#Excepcion para controlar una mala traduccion del individo, solo por precaucion(En teoria no deberia ocurrir nunca)
       ErrorFlag=1
   #############################################################################
   try:
       vR2a=np.real(vR2c)
       pass
   except ValueError:
       vR2a=NaN
       ErrorFlag=1
       pass
   except ZeroDivisionError:
       vR2a=NaN
       zeroflag=1
       pass
   except OverflowError:#Excepcion para penalizar que al momento de evaluar el individuo ocurra: division por cero, o algun error por sobreflujo(valor enorme en extremo)
       vR2a=math.inf
       OverFlag=1
       pass
   except (TypeError,MemoryError):#Excepcion para evitar operaciones con complejos y no complejos, y problemas de indeterminacion entre funciones que algun valor no este entre su dominio
       print(vR2c)
       print("\nSimulacion terminada por maximo de memoria consumido\n")
       sys.exit()
   try:
       vR2b=(np.real(cmath.log(np.abs(cmath.log(cmath.cos(cmath.log(np.linalg.norm(Minus(q1,OrR1R1)))))))*cmath.log(np.linalg.norm(Minus(q1,OrR1R1)))))+(np.real(cmath.log(np.abs(cmath.log(cmath.cos(cmath.log(np.linalg.norm(Minus(q2,OrR2R1)))))))*cmath.log(np.linalg.norm(Minus(q2,OrR2R1)))))
   except ValueError:#Excepcion para controlar una indefinicion de las funciones, solo por precaucion(En teoria no deberia ocurrir nunca)
       vR2b=NaN
       TypeFlag=1     
   vR2=Plus(vR2a,vR2b)
   vxaR2=xdp2+k1R2*(xd2-q2[0])
   if len([vR2])>1:
    vxrR2=Times(vR2[0],(yd2-q2[1]))
   else:
    vxrR2=Times(vR2,(yd2-q2[1]))
   vxR2=Plus(vxaR2,vxrR2)
   vyaR2=ydp2+k2R2*(yd2-q2[1])
   if len([vR2])>1:
    vyrR2=Times(Times(-1,vR2[0]),(xd2-q2[0]))
   else:
    vyrR2=Times(Times(-1,vR2),(xd2-q2[0]))
   vyR2=Plus(vyaR2,vyrR2)
   FlagsR2=[zeroflag,ErrorFlag,OverFlag,TypeFlag]
   resR2=list(Real([vxR2,vyR2]))
   return FlagsR2, resR2


