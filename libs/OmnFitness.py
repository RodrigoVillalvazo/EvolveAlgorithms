import csv
import sys
import numpy as np
import math
sys.path.insert(0, '~/libs')
sys.path.insert(1, '~/Simulation')
from Simulations.Simulate import Simulacion
from libs.Math import Plus, Times
class OmnFitness:
    def __init__(self,ind):
        self.ind = ind
    def DesTime(self,td):
        self.td = td
    def Fitness(self,index):
            ret_fit1=0
            ret_fit3=0
            FileD=open('Training.txt')#Direccion contenedora del archivo de condiciones iniciales
            #td=self.td
            ind=self.ind
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
            rCen=0.1
            n=2
            #Vector direccion
            theta=np.arange(0,2*np.pi,2*np.pi/n)
            Vdir1=[np.cos(theta[0]),np.sin(theta[0])]
            Vdir2=[np.cos(theta[1]),np.sin(theta[1])]
            #Posicion deseada
            PdR1=Plus(Cd,Times(rCen,Vdir1))
            PdR2=Plus(Cd,Times(rCen,Vdir2))   
            #Hacemos un barrido de las condiciones inciales y accedemos a las que necesitemos
            Rob1=[lineData[0][index],lineData[1][index]]#Posicion inicial del robot 1
            Rob2=[lineData[2][index],lineData[3][index]]#Posicion inicial del robot 2
            td=float(lineData[6][index])
            tf=td+0.50
            initialConditions=[Rob1,Rob2,PdR1,PdR2]#Vector de Condiciones iniciales
            radios=[0.02,0.02]#Radio de los robots y obstaculos
            pd=[initialConditions[2],initialConditions[3]]#Vectir de posiciones deseadas
            s=Simulacion(ind=ind,pos=initialConditions,pd=pd,r=radios,tf=tf,td=td)#Simulacion de los robots para cada condicion inicial y cada individuo
            #Tiempo que tardo en llegar el robot
            timeSavedR1=s[0]
            timeSavedR2=s[1]
            Try1a=s[2]#Posicion en el eje X del robot 1
            Try2a=s[3]#Posicion en el eje Y del robot 1
            Try3a=s[4]#Posicion en el eje X del robot 2
            Try4a=s[5]#Posicion en el eje Y del robot 2
            
            dsR1=s[12]#Distancia entre cada robot visto desde el robot 1
            dsR2=s[13]#Distancia entre cada robot visto desde el robot 2
            #Variable temporal almacendada para cada robot
            timeR1=s[14]#Variable t del robot 1
            timeR2=s[15]#Variable t del robot 2
                
            n1=np.size(timeR1)-1#Variable auxiliar
            n2=np.size(timeR2)-1#Variable auxiliar
                        
                        
            ErrorPosRob1=np.linalg.norm([Try1a[n1]-PdR1[0],Try2a[n1]-PdR1[1]])#Error de posicion del robot 1
            ErrorPosRob2=np.linalg.norm([Try3a[n1]-PdR2[0],Try4a[n1]-PdR2[1]])#Error de posicion del robot 2
            ErrorTiempoR1=abs(timeSavedR1-td)#Error del tiempo de llegada del robot 1 y el tiempo limite
            ErrorTiempoR2=abs(timeSavedR2-td)#Error del tiempo de llegada del robot 2 y el tiempo limite
            radio=radios[0]+radios[1]
            tolerance=0.3
            Ext1=(timeSavedR1==0)and(ErrorTiempoR1>tolerance)
            Ext2=(timeSavedR2==0)and(ErrorTiempoR2>tolerance)
            old_fitness=(ErrorPosRob1**2)+(ErrorPosRob2**2)+(ErrorTiempoR1**2)+(ErrorTiempoR2**2)#Fitness error cuadratico medio
            
            if (math.isnan(old_fitness) or math.isinf(old_fitness)):#Penalizamos si el fitness es infinito o si no es un numero
                ret_fit1=old_fitness+50.0
            elif(Ext1 or Ext2):#Penalizamos la diferencia entre tiempos de llegada de cada robot
                ret_fit3=old_fitness+40.0
            else:
                old_fitness=old_fitness
            new_fitness=ret_fit1+ret_fit3+old_fitness#Fitness error cuadratico medio 
            return new_fitness,      