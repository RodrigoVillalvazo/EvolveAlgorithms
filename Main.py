# importing sys
import sys
import signal
# adding Folder_2/subfolder to the system path
sys.path.insert(0, '~/libs')
sys.path.insert(1, '~/Simulation')
from libs.Math import Plus, Minus, Divide, Times,Power, Maximum, Minimum, Atan2r
from libs.Math import Sqrt, Sqr, Logn, Exp, Sinh, Cosh, Tanh, Csch, Sech, Coth, Cos, Sin, Tan, Csc, Sec, Cot, Asin, Acos, Norm, Abs, Real, Atanr
from libs import AlgorithmMod
from libs import OmnFitness

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
N=2
def Main(N,path):
    CPU_count = MP.cpu_count()-1
    start = time.time()
    #   Algoritmo de Programacion Genetica para evolucionar
    #   un modelo de navegación de un robot movil.
    #   Version: 1.14.17092024
    #   Autor: MSc. Rodrigo A. Villalvazo Covian
    #   Posgrado de Control y Robótica
    #   ITE, Ensenada B.C. Mexico
    """
    Program and Problem parameters
    """
    #Tiempo de llegada
    td=4.0
    #numero de generaciones
    Ngen=100#increase Factor
    #numero de poblacion
    Npop=300#Decrease factor
    #numero de condiciones iniciales disponibles
    Ncon=10
    #condicionador, el factor debe ser menor al numero de condiciones
    #Factor=Factorial*round(Ngen*((abs(((CPU_count*Ncon)*0.25)-Ncon))/Npop))#Factor de condicion para procesos respecto a las condiciones disponibles
    Proc=2
    #Numero de corrida
    run=int(N)
    #Participantes en el torneo
    winners=7
    def MultProcess(ind,td,Npros,Ncon):
        Fit=OmnFitness.OmnFitness(ind)
        Fit.DesTime(td)
        i=[]
        TimeExec='TimeByExecution.csv'
        FILEGTIME=open(TimeExec,'a')
        firstTime=time.time()
        with MP.Pool(processes=Npros) as pool:
            sys.stdout.flush()
            #multiple_results = [pool.apply_async(Fit.Fitness, args=(i,)) for i in range(Ncon)]
            multiple_results = pool.map_async(Fit.Fitness, range(Ncon))
            #multiple_results = [pool.map_async(Fit.Fitness, args=(i,)) for i in range(Ncon)]
            multiple_results.wait(timeout=(600/Npros))
            if multiple_results.ready():
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
                pool.terminate()
                pool.join()
        Values=multiple_results._value
        if (conn==True):
            for j in range(Ncon):
                try:
                    if(Values[j] is None):
                        Values[j]=140.0
                    else:
                        Values[j]=Values[j][0]
                except:
                    Values=[130.0]
                    break
            pass
            mfitness=Values
            #break
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
    pset = gp.PrimitiveSetTyped("MAIN",itertools.repeat(float,26),float)
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
    #Terminales
    pset.addTerminal("qx2",str)#0
    pset.addTerminal("qy2",str)#1
    pset.addTerminal("qx1",str)#2
    pset.addTerminal("qy1",str)#3
    pset.addTerminal("xd1",str)#4
    pset.addTerminal("xdp1",str)#5
    pset.addTerminal("yd1",str)#6
    pset.addTerminal("ydp1",str)#7
    pset.addTerminal("xd2",str)#8
    pset.addTerminal("xdp2",str)#9
    pset.addTerminal("yd2",str)#10
    pset.addTerminal("ydp2",str)#11
    pset.addTerminal("Vx1",str)#12
    pset.addTerminal("Vy1",str)#13
    pset.addTerminal("Vx2",str)#14
    pset.addTerminal("Vy2",str)#15
    pset.addTerminal("t1",str)#16   
    pset.addTerminal("t2",str)#17
    pset.addTerminal("td",str)#18
    pset.addTerminal("q1",str)#21
    pset.addTerminal("q2",str)#22
    pset.addTerminal("qd1",str)#23
    pset.addTerminal("qd2",str)#24
    pset.addTerminal("V1",str)#25
    pset.addTerminal("V2",str)#26
    pset.addTerminal("tR",str)#27
    pset.addTerminal("tdR",str)#28
    #pset.addTerminal("OrR1R1",str)#19
    #pset.addTerminal("OrR2R1",str)#20
    """Rename the Args to our variables names"""
    pset.renameArguments(ARG0='qx2')
    pset.renameArguments(ARG1='qy2')
    pset.renameArguments(ARG2='qx1')
    pset.renameArguments(ARG3='qy1')
    pset.renameArguments(ARG4='xd1')
    pset.renameArguments(ARG5='xdp1')
    pset.renameArguments(ARG6='yd1')
    pset.renameArguments(ARG7='ydp1')
    pset.renameArguments(ARG8='xd2')
    pset.renameArguments(ARG9='xdp2')
    pset.renameArguments(ARG10='yd2')
    pset.renameArguments(ARG11='ydp2')
    pset.renameArguments(ARG12='Vx1')
    pset.renameArguments(ARG13='Vy1')
    pset.renameArguments(ARG14='Vx2')
    pset.renameArguments(ARG15='Vy2')
    pset.renameArguments(ARG16='t1')
    pset.renameArguments(ARG17='t2')
    pset.renameArguments(ARG18='td')
    pset.renameArguments(ARG19='q1')
    pset.renameArguments(ARG20='q2')
    pset.renameArguments(ARG21='qd1')
    pset.renameArguments(ARG22='qd2')
    pset.renameArguments(ARG23='V1')
    pset.renameArguments(ARG24='V2')
    pset.renameArguments(ARG25='tR')
    pset.renameArguments(ARG26='tdR')
    #pset.renameArguments(ARG19='OrR1R1')
    #pset.renameArguments(ARG20='OrR2R1')
    """Get the indiviual expresion"""
    #expr = toolbox.individual()
    #del pset
    gc.collect()
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
    chk_name=str('checkpoint'+str(run)+'.pkl')
    newCheckP=path+chk_name
    CheckP=AlgorithmMod.CheckPoint(newCheckP,path,chk_name)
    try:
        pop, log = AlgorithmMod.eaSimpleModWithElitism(path,newCheckP,pop, toolbox, 0.80, 0.20, Ngen, run, 1,stats=mstats,
                                        halloffame=hof,checkpoint=CheckP,verbose=True)
    except:
        traceback.print_exc()

    try:
        best = hof.items[0]
    except:
        input("Press Enter to continue...")
        os.kill(os.getpid(), signal.SIGTERM)

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
    os.kill(os.getpid(), signal.SIGTERM)
if __name__=="__main__":
    MP.freeze_support()
    #Directorio donde se almacenaran todos los datos
    pathA =str('Results/')
    pathB =str('Corrida'+str(N)+'/')
    path=pathA+pathB
    #Instrucciones para crear el directorio
    try:
        #Se intenta crear el directorio
        #Si no hay ninguno de nombre repetido se crea una nueva carpeta
        os.mkdir(pathA)
        #imprimimos un texto al usuario si se creo la carpeta
        sys.stdout.write("\nCreacion completa del directorio: %s\n"%pathA)
        sys.stdout.flush()
        #Accedemos a la simulacion y parametros evolutivas
    except OSError:
        gc.collect()
        #Si la carpeta ya existe se muestra al usuario un texto avisando que la carpeta sera sobreescribida
        sys.stdout.flush()   
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
    Main(N,path)
"""
Create the fitness class
:param ind => Individual from DEAP toolbox
:param td => Desired time
:param Npros => Number of initial conditions
"""
