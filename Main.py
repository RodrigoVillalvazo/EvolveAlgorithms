# importing sys
import sys
# adding Folder_2/subfolder to the system path
sys.path.insert(0, '~/libs')
sys.path.insert(1, '~/Simulation')
from libs.Math import Plus, Minus, Divide, Times,Power, Maximum, Minimum, Atan2r
from libs.Math import Sqrt, Sqr, Logn, Exp, Sinh, Cosh, Tanh, Csch, Sech, Coth, Cos, Sin, Tan, Csc, Sec, Cot, Asin, Acos, Norm, Abs, Real, Atanr
from Simulations.Simulate import Evasion2Robots
from libs import AlgorithmMod

#No-Downlodable
import gc
import os
import csv
import time
import math
import socket
import itertools
import traceback
import multiprocessing as MP
#Downlodable
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from deap import tools
from deap import gp
from deap import creator
from deap import base

N=0
CPU_count = MP.cpu_count()-1
start = time.time()
#   Algoritmo de Programacion Genetica para evolucionar
#   un modelo de navegación de un robot movil.
#   Version: 1.14.21122022
#   Autor: MSc. Rodrigo A. Villalvazo Covian
#   Posgrado de Control y Robótica
#   ITE, Ensenada B.C. Mexico
"""
Program and Problem parameters
"""
#Tiempo de llegada
td=4.0
#numero de generaciones
Ngen=10#increase Factor
#numero de poblacion
Npop=10#Decrease factor
#numero de condiciones iniciales disponibles
Ncon=10
#condicionador, el factor debe ser menor al numero de condiciones
#Factor=Factorial*round(Ngen*((abs(((CPU_count*Ncon)*0.25)-Ncon))/Npop))#Factor de condicion para procesos respecto a las condiciones disponibles
Proc=9
#Numero de corrida
run=int(N)
#Participantes en el torneo
if(Npop>=10):
    winners=7
else:
    winners=1
class MyFitness:
    def __init__(self,ind):
        self.ind = ind
    def DesTime(self,td):
        self.td = td
    def Fitness(self,Npros):
            FileD=open('Training.txt')#Direccion contenedora del archivo de condiciones iniciales
            td=self.td
            ind=self.ind
            i=Npros
            #tf=lineData[5][i]#Tiempo de simulacion
            #Variabl
            nk=0
            ne=0
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
            Rob1=[lineData[0][i],lineData[1][i]]#Posicion inicial del robot 1
            Rob2=[lineData[2][i],lineData[3][i]]#Posicion inicial del robot 2
            #td=float(eval(str(lineData[6][i]).replace('"', '').replace("'", '')))
            tf=4.50
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
            EX1=s[24]
            EX2=s[25]
            EX3=s[26]
            EX4=s[27]
                
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
            if(EX1>0)or(EX2>0):
                fitness=math.NaN
            elif(EX3>0):
                fitness=math.Inf
            else:
                fitness=(ErrorPosRob1**2)+(ErrorPosRob2**2)+(ErrorTiempoR1**2)+(ErrorTiempoR2**2)#Fitness error cuadratico medio
            if (math.isnan(fitness) or math.isinf(fitness)):#Penalizamos si el fitness es infinito o si no es un numero
                fitness=5000000.0;
                #nfa=nfa+1;
            elif((dsR1<=radio)and(dsR2<=radio)):
                fitness=3000000.0;
            elif((timeSavedR1==0)and(ErrorTiempoR1>tolerance)):#Penalizamos la diferencia entre tiempos de llegada de cada robot
                fitness=4000000.0
            elif((timeSavedR2==0)and(ErrorTiempoR2>tolerance)):#Penalizamos la diferencia entre tiempos de llegada de cada robot
                fitness=4000000.0
            elif((RuntimeWarning==True)or(RuntimeError==True)or(ValueError==True)):
                fitness=6000000.0
            else:
                fitness=(ErrorPosRob1**2)+(ErrorPosRob2**2)+(ErrorTiempoR1**2)+(ErrorTiempoR2**2)#Fitness error cuadratico medio
            return fitness,      
def MultProcess(ind,td,Npros,Ncon):
    Fit=MyFitness(ind)
    Fit.DesTime(td)
    i=[]
    TimeExec='TimeByExecution.csv'
    FILEGTIME=open(TimeExec,'a')
    firstTime=time.time()
    #time.sleep(1)
    #AlgorithmMod.update_progress("Starting pool", 1)
    #sys.stdout.write("\nStarting pool\n")
    #obj = socket.socket()
    with MP.Pool(processes=Npros) as pool:
        sys.stdout.flush()
        #multiple_results = [pool.apply_async(Fit.Fitness, args=(i,)) for i in range(Ncon)]
        multiple_results = pool.map_async(Fit.Fitness, range(Ncon))
        #multiple_results = [pool.map_async(Fit.Fitness, args=(i,)) for i in range(Ncon)]
        #if len(multiple_results._cache)>2e3:
        #sys.stdout.write("\nEsperando limpieza de cache\n")
        multiple_results.wait(timeout=70)
        if multiple_results.ready():
            #AlgorithmMod.update_msg("Pool Ready", 1)
            #sys.stdout.write("\nPool Ready\n")
            conn=False
            pool.close()
            pool.join()
        elif(socket.error==True):
            AlgorithmMod.update_msg("Socket Disconected", 1)
            conn=True
            pool.terminate()
            pool.join()
        else:
            conn=True
            AlgorithmMod.update_msg("Pool Not Ready Yet Killing threads", 1)
            #sys.stdout.write("\nPool Not Ready Yet Killing childs\n")
            pool.terminate()
            pool.join()
    Values=multiple_results._value
    while (conn==True):
        for j in range(Ncon):
            try:
                if(Values[j] is None):
                    Values[j]=7000000.0
                else:
                    Values[j]=Values[j][0]
            except:
                Values=[8000000.0]
                break
        pass
        mfitness=Values
        #mfitness=multiple_results
      #  try:
         #   obj.connect(host)
       # except:
          #  obj.close()
        break
    else:
        mfitness=Values
    #break
    try:
        MYFitness=np.mean(mfitness)
    except:
        AlgorithmMod.update_msg(Values, 1)
        AlgorithmMod.update_msg(str(ind), 1)
        MYFitness=np.mean([mfitness])
    lastTime=time.time()
    totalTime=lastTime-firstTime
    FILEGTIME.write(f"First Time: {firstTime};"+f" Last Time: {lastTime};"+f" Total Time(s): {totalTime};")
    FILEGTIME.write('\n')
    FILEGTIME.close()
    return MYFitness,     


toolbox = base.Toolbox()
OutARGS=[float,float,float,float,float,float,float,float,float,float]
#pset = gp.PrimitiveSetTyped("main",NumARGS,float)
pset = gp.PrimitiveSetTyped("MAIN",itertools.repeat(float,28),float)
time.sleep(0.01)
#history = tools.History()
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin,pset=pset)
# Attribute generator
toolbox.register("expr_init", gp.genHalfAndHalf, pset=pset, min_=1, max_=11)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr_init)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate",MultProcess,td=td,Npros=Proc,Ncon=Ncon)
toolbox.register("select", tools.selTournament, tournsize=winners)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=1, max_=11)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)
# Decorate the variation operators
#toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=11))
#toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("weigth"), max_value=11))
#toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=11))    
#toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("weigth"), max_value=11))    
#Parametros
pset.addPrimitive(Plus,[float,float],float)#Suma normalizada
pset.addPrimitive(Minus,[float,float],float)#Resta normalizada
pset.addPrimitive(Divide,[float,float],float)#Division Real normalizada
pset.addPrimitive(Times,[float,float],float)#Multiplicacion normalizada
pset.addPrimitive(Power,[float,float],float)#Exponenciacion
pset.addPrimitive(Maximum,[float,float],float)#Valor maximo
pset.addPrimitive(Minimum,[float,float],float)#Valor minimo
pset.addPrimitive(Atan2r,[float,float],float)#arcotangente real de 2 valores normalizada
#Arity 1
pset.addPrimitive(Sqrt,[float],float)#Raiz cuadrada
pset.addPrimitive(Sqr,[float],float)#Cuadrado de un escalar
pset.addPrimitive(Logn,[float],float)#Logaritmo
pset.addPrimitive(Exp,[float],float)#Exponencial
pset.addPrimitive(Sinh,[float],float)#Seno hyperbolico
pset.addPrimitive(Cosh,[float],float)#Coseno hyperbolico
pset.addPrimitive(Tanh,[float],float)#Tangente hyperbolica
pset.addPrimitive(Csch,[float],float)#Cosecante hyperbolico
pset.addPrimitive(Sech,[float],float)#Secante hyperobolica
pset.addPrimitive(Coth,[float],float)#Cotangente hyperbolico
pset.addPrimitive(Cos,[float],float)#coseno
pset.addPrimitive(Sin,[float],float)#seno
pset.addPrimitive(Tan,[float],float)#tangente
pset.addPrimitive(Csc,[float],float)#cosecante
pset.addPrimitive(Sec,[float],float)#secante
pset.addPrimitive(Cot,[float],float)#cotangente
pset.addPrimitive(Asin,[float],float)#Arcoseno
pset.addPrimitive(Acos,[float],float)#Arcocoseno
pset.addPrimitive(Norm,[float],float)#norma
pset.addPrimitive(Abs,[float],float)#absoluto
pset.addPrimitive(Real,[float],float)#real
pset.addPrimitive(Atanr,[float],float)#arcotangente real
#Arity 3 or special operators
#pset.addPrimitive(Integrate,[float,float],float)#arcotangente real
#pset.addPrimitive(TrigSimp,[float],float)#arcotangente real
#pset.addPrimitive(FFT,[float,float],float)#arcotangente real
#Terminales
pset.addTerminal("q1",str)#0
pset.addTerminal("q2",str)#1
pset.addTerminal("qx2",str)#2
pset.addTerminal("qy2",str)#3
pset.addTerminal("qx1",str)#4
pset.addTerminal("qy1",str)#5
pset.addTerminal("xd1",str)#6
pset.addTerminal("xdp1",str)#7
pset.addTerminal("yd1",str)#8
pset.addTerminal("ydp1",str)#9
pset.addTerminal("xd2",str)#10
pset.addTerminal("xdp2",str)#11
pset.addTerminal("yd2",str)#12
pset.addTerminal("ydp2",str)#13
pset.addTerminal("Vx1",str)#14
pset.addTerminal("Vy1",str)#15
pset.addTerminal("Vx2",str)#16
pset.addTerminal("Vy2",str)#17
pset.addTerminal("qd1",str)#18
pset.addTerminal("qd2",str)#19
pset.addTerminal("V1",str)#20
pset.addTerminal("V2",str)#21
pset.addTerminal("t1",str)#22   
pset.addTerminal("t2",str)#23
pset.addTerminal("tR",str)#24
pset.addTerminal("td",str)#25
pset.addTerminal("tdR",str)#26
pset.addTerminal("OrR1R1",str)#27
pset.addTerminal("OrR2R1",str)#28
"""Rename the Args to our variables names"""
pset.renameArguments(ARG0='q1')
pset.renameArguments(ARG1='q2')
pset.renameArguments(ARG2='qx2')
pset.renameArguments(ARG3='qy2')
pset.renameArguments(ARG4='qx1')
pset.renameArguments(ARG5='qy1')
pset.renameArguments(ARG6='xd1')
pset.renameArguments(ARG7='xdp1')
pset.renameArguments(ARG8='yd1')
pset.renameArguments(ARG9='ydp1')
pset.renameArguments(ARG10='xd2')
pset.renameArguments(ARG11='xdp2')
pset.renameArguments(ARG12='yd2')
pset.renameArguments(ARG13='ydp2')
pset.renameArguments(ARG14='Vx1')
pset.renameArguments(ARG15='Vy1')
pset.renameArguments(ARG16='Vx2')
pset.renameArguments(ARG17='Vy2')
pset.renameArguments(ARG18='qd1')
pset.renameArguments(ARG19='qd2')
pset.renameArguments(ARG20='V1')
pset.renameArguments(ARG21='V2')
pset.renameArguments(ARG22='t1')
pset.renameArguments(ARG23='t2')
pset.renameArguments(ARG24='tR')
pset.renameArguments(ARG25='td')
pset.renameArguments(ARG26='tdR')
pset.renameArguments(ARG27='OrR1R1')
pset.renameArguments(ARG28='OrR2R1')
"""Get the indiviual expresion"""
expr = toolbox.individual()
del pset
gc.collect()
if __name__=="__main__":
    MP.freeze_support()
    #Directorio donde se almacenaran todos los datos
    path =str('Corrida'+str(run)+'/')
    #Instrucciones para crear el directorio
    try:
        #Se intenta crear el directorio
        #Si no hay ninguno de nombre repetido se crea una nueva carpeta
        os.mkdir(path)
        #imprimimos un texto al usuario si se creo la carpeta
        sys.stdout.write("\nCreacion completa del directorio: %s\n"%path)
        sys.stdout.flush()
        #Accedemos a la simulacion y parametros evolutivas
    except OSError:
        gc.collect()
        #Si la carpeta ya existe se muestra al usuario un texto avisando que la carpeta sera sobreescribida
        sys.stdout.flush()   
    #Estadisticas
    stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
    stats_size = tools.Statistics(len)
    mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
    mstats.register("avg", np.mean)
    mstats.register("std", np.std)
    mstats.register("min", np.min)
    mstats.register("max", np.max)
    pop = toolbox.population(n=Npop)
    hof = tools.HallOfFame(1)
    newCheckP=str('checkpoint'+str(run)+'.pkl')
    CheckP=AlgorithmMod.CheckPoint(newCheckP)
    try:
        pop, log = AlgorithmMod.eaSimpleModWithElitism(path,newCheckP,pop, toolbox, 0.80, 0.20, Ngen, run, 1,stats=mstats,
                                        halloffame=hof,checkpoint=CheckP,verbose=True)
    except:
        traceback.print_exc()

    try:
        best = hof.items[0]
    except:
        input("Press Enter to continue...")
        os.kill(os.getpid(), MP.signal.SIGTERM)

    bestFitness= best.fitness.values[0]
    #Extract statistics
    minFitnessValues, meanFitnessValues=log.chapters["fitness"].select("min","avg")
    #plot statistics
    sns.set_style("whitegrid")
    plt.plot(minFitnessValues,marker='*', color='red')
    plt.xlabel('Generation')
    plt.ylabel('Min Fitness')
    plt.title('Min Fitness over Generations')
    plt.savefig(path+'Statistics'+str(run)+'.eps')
    plt.savefig(path+'Statistics'+str(run)+'.png')
    plt.close()
    end = time.time()
    finaltime=end-start
    print("Multiprocessing with",CPU_count,"core(s) took",round(finaltime,2),"s")
    #Calculamos el tiempo transcurrido de la ejecucion del programa
    #Imprimimos en segundos
    if(finaltime<=60):
        sys.stdout.write("\nTiempo transcurrido: %f seg\n"%(finaltime))
    #Imprimimos en minutos
    elif(finaltime>60)and(finaltime<3600):
        sys.stdout.write("\nTiempo transcurrido: %f min\n"%(finaltime/60))
    #Imprimimos en horas
    elif(finaltime>3600)and(finaltime<86400):
        sys.stdout.write("\nTiempo transcurrido: %f horas\n"%(finaltime/3600))
    #Imprimimos en dias
    elif(finaltime>86400)and(finaltime<2678000):
        sys.stdout.write("\nTiempo transcurrido: %f dias\n"%(finaltime/86400))
    #Finalizamos el programa
    input("Press Enter to continue...")
    os.kill(os.getpid(), MP.signal.SIGTERM)
"""
Create the fitness class
:param ind => Individual from DEAP toolbox
:param td => Desired time
:param Npros => Number of initial conditions
"""