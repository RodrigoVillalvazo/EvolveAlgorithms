#!/usr/bin/env python3
import sys, os
import time
import numpy as np
import multiprocessing as MP
import socket
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
# adding Folder_2/subfolder to the system path
from libs.AlgorithmMod import update_msg
from libs.OmnFitness import OmnFitness
def Main():
    ind='Sin(0)'
    #td=4.0
    Npros=2
    Ncon=10
    Fit=OmnFitness(ind)
    #Fit.DesTime(td)
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
            update_msg("Socket Disconected", 1)
            conn=True
            pool.terminate()
            pool.join()
        else:
            conn=True
            update_msg("Pool Not Ready Yet Killing threads", 1)
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
        #mfitness=multiple_results
        #break
    else:
        mfitness=Values
    #break
    try:
        MYFitness=np.mean(mfitness)
    except:
        update_msg(Values, 1)
        update_msg(str(ind), 1)
        MYFitness=np.mean([mfitness])
    lastTime=time.time()
    totalTime=lastTime-firstTime
    return MYFitness,totalTime
if __name__=="__main__":
    MP.freeze_support()
    res,tiM = Main()
    print("Elapsed time: "+str(tiM) + "Mean Fitness: " + str(np.mean(res)))
