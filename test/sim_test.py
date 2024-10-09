#!/usr/bin/env python3
import csv
import numpy as np
import math
import time
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Simulations.Simulate2 import Evasion2Robots
firstTime=time.time()
fit=[]
for i in range (10):
    ret_fit1=0
    ret_fit2=0
    ret_fit3=0
    FileD=open('Training.txt')#Direccion contenedora del archivo de condiciones iniciales
    #td=4.0
    index=i
    #ind='Power(Abs(Sec(xd2)), tR)'
    ind='Sin(Vy1)'
    #ind='Logn(Sqrt(Norm(xdp2)))'
    reader=csv.reader(FileD, delimiter=' ',skipinitialspace=True)#Leemos todo el documento
    lineData = list()#variable para las lineas
    cols=next(reader)#variable para las columnas
    #  Leemos las columnas
    for col in cols:
        lineData.append(list())
    #Leemos las lineas
    for line in reader:
        for j in range(0,len(lineData)):
            lineData[j].append(line[j])
    #Guardamos el resultado como un diccionario
    data=dict()
    for j in range(0, len(cols)):
        data[j]=lineData[j]
    Cd=[0.5,0.5]
    #Hacemos un barrido de las condiciones inciales y accedemos a las que necesitemos
    Rob1=[lineData[0][index],lineData[1][index]]#Posicion inicial del robot 1
    Rob2=[lineData[2][index],lineData[3][index]]#Posicion inicial del robot 2
    td=float(lineData[6][index])
    tf=td+0.50
    rRob1,rRob2=0.02,0.02#Radio del robot 1 y robot2
    s,Desires=Evasion2Robots(ind,tf,td,FileD,Rob1,Rob2,rRob1,rRob2,Cd)#Simulacion de los robots para cada condicion inicial y cada individuo
    radios=Desires[0]
    pd=Desires[1]
    PdR1=pd[0]
    PdR2=pd[1]
    #Tiempo que tardo en llegar el robot
    timeSavedR1=s[0]
    timeSavedR2=s[1]
    #Variable temporal almacendada para cada robot
    timeR1=s[5]#Variable t del robot 1
    timeR2=s[19]#Variable t del robot 2
    Try1=s[2]#Posicion en el eje X del robot 1
    Try2=s[10]#Posicion en el eje Y del robot 1
    Try3=s[11]#Posicion en el eje X del robot 2
    Try4=s[12]#Posicion en el eje Y del robot 2
    dsR1=s[20]#Distancia entre cada robot visto desde el robot 1
    dsR2=s[21]#Distancia entre cada robot visto desde el robot 2
    n1=np.size(timeR1)-1#Variable auxiliar
    n2=np.size(timeR2)-1#Variable auxiliar
                
    TryR1=[Try1[n1],Try2[n1]]#Vector posicion del robot 1
    TryR2=[Try3[n2],Try4[n2]]#Vector posicion del robot 2
                
    ErrorPosRob1=np.linalg.norm([TryR1[0]-PdR1[0],TryR1[1]-PdR1[1]])#Error de posicion del robot 1
    ErrorPosRob2=np.linalg.norm([TryR2[0]-PdR2[0],TryR2[1]-PdR2[1]])#Error de posicion del robot 2
    ErrorTiempoR1=abs(timeSavedR1-td)#Error del tiempo de llegada del robot 1 y el tiempo limite
    ErrorTiempoR2=abs(timeSavedR2-td)#Error del tiempo de llegada del robot 2 y el tiempo limite
    radio=radios[0]+radios[1]
    tolerance=0.3
    Ext1=(timeSavedR1==0)and(ErrorTiempoR1>tolerance)
    Ext2=(timeSavedR2==0)and(ErrorTiempoR2>tolerance)

    old_fitness=(ErrorPosRob1**2)+(ErrorPosRob2**2)+(ErrorTiempoR1**2)+(ErrorTiempoR2**2)#Fitness error cuadratico medio
    print("Before restrictions "+str(old_fitness))  
    if (math.isnan(old_fitness) or math.isinf(old_fitness)):#Penalizamos si el fitness es infinito o si no es un numero
        ret_fit1=old_fitness+120.0
    elif((dsR1<=radio)and(dsR2<=radio)):
        ret_fit2=old_fitness+100.0
    elif(Ext1 or Ext2):#Penalizamos la diferencia entre tiempos de llegada de cada robot
        ret_fit3=old_fitness+110.0
    else:
        old_fitness=old_fitness
    new_fitness=ret_fit1+ret_fit2+ret_fit3+old_fitness#Fitness error cuadratico medio 
    fit.append(new_fitness)
    print("After restrictions "+str(new_fitness)+"  "+str(ErrorPosRob1)+"  "+str(ErrorPosRob2)+"  "+str(ErrorTiempoR1)+"  "+str(ErrorTiempoR2)+'\n')  
    '''Create the path frame'''
    fig=plt.figure()
    plt.plot(Try1,Try2,Try3,Try4)
    plt.plot(PdR1[0],PdR1[1],'*')
    plt.plot(PdR2[0],PdR2[1],'*')
    plt.grid(True)
    plt.show()

lastTime=time.time()
totalTime=lastTime-firstTime
print("Elapsed time: "+str(totalTime) + "Mean Fitness: " + str(np.mean(fit)))