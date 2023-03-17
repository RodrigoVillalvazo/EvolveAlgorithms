import time
import random
import sys
import tracemalloc
import os
import pickle
from deap import tools
def update_progress(job_title, progress):
    try:
        os.system('clc')
    except:
        os.system('clear')
    finally:
        os.system('cls')
    length = 20 # modify this to change the length
    block = int(round(length*progress))
    msg = "\r{0}: [{1}] {2}%".format(job_title, "#"*block + "-"*(length-block), round(progress*100, 2))
    if progress >= 1: msg += " DONE\r\n"
    sys.stdout.write(msg)
    sys.stdout.flush()

def update_msg(job, prog):
    length2 = 20 # modify this to change the length
    block2 = int(round(length2*prog))
    msg2 = "\n{0}: [{1}] {2}%".format(job, "#"*block2 + "-"*(length2-block2), round(prog*100, 2))
    if prog >= 1: msg2 += " DONE\n"
    sys.stdout.write(msg2)
    sys.stdout.flush() 

def varAnd(population, toolbox, cxpb, mutpb):
    """Part of an evolutionary algorithm applying only the variation part
    (crossover **and** mutation). The modified individuals have their
    fitness invalidated. The individuals are cloned so returned population is
    independent of the input population.

    :param population: A list of individuals to vary.
    :param toolbox: A :class:`~deap.base.Toolbox` that contains the evolution
                    operators.
    :param cxpb: The probability of mating two individuals.
    :param mutpb: The probability of mutating an individual.
    :returns: A list of varied individuals that are independent of their
              parents.

    The variation goes as follow. First, the parental population
    :math:`P_\mathrm{p}` is duplicated using the :meth:`toolbox.clone` method
    and the result is put into the offspring population :math:`P_\mathrm{o}`.  A
    first loop over :math:`P_\mathrm{o}` is executed to mate pairs of
    consecutive individuals. According to the crossover probability *cxpb*, the
    individuals :math:`\mathbf{x}_i` and :math:`\mathbf{x}_{i+1}` are mated
    using the :meth:`toolbox.mate` method. The resulting children
    :math:`\mathbf{y}_i` and :math:`\mathbf{y}_{i+1}` replace their respective
    parents in :math:`P_\mathrm{o}`. A second loop over the resulting
    :math:`P_\mathrm{o}` is executed to mutate every individual with a
    probability *mutpb*. When an individual is mutated it replaces its not
    mutated version in :math:`P_\mathrm{o}`. The resulting :math:`P_\mathrm{o}`
    is returned.

    This variation is named *And* because of its propensity to apply both
    crossover and mutation on the individuals. Note that both operators are
    not applied systematically, the resulting individuals can be generated from
    crossover only, mutation only, crossover and mutation, and reproduction
    according to the given probabilities. Both probabilities should be in
    :math:`[0, 1]`.
    """
    offspring = [toolbox.clone(ind) for ind in population]

    # Apply crossover and mutation on the offspring
    for i in range(1, len(offspring), 2):
        if random.random() < cxpb:
            offspring[i - 1], offspring[i] = toolbox.mate(offspring[i - 1],
                                                          offspring[i])
            del offspring[i - 1].fitness.values, offspring[i].fitness.values

    for i in range(len(offspring)):
        if random.random() < mutpb:
            offspring[i], = toolbox.mutate(offspring[i])
            del offspring[i].fitness.values

    return offspring
def varOr(population, toolbox, lambda_, cxpb, mutpb):
    """Part of an evolutionary algorithm applying only the variation part
    (crossover, mutation **or** reproduction). The modified individuals have
    their fitness invalidated. The individuals are cloned so returned
    population is independent of the input population.

    :param population: A list of individuals to vary.
    :param toolbox: A :class:`~deap.base.Toolbox` that contains the evolution
                    operators.
    :param lambda\_: The number of children to produce
    :param cxpb: The probability of mating two individuals.
    :param mutpb: The probability of mutating an individual.
    :returns: The final population.

    The variation goes as follow. On each of the *lambda_* iteration, it
    selects one of the three operations; crossover, mutation or reproduction.
    In the case of a crossover, two individuals are selected at random from
    the parental population :math:`P_\mathrm{p}`, those individuals are cloned
    using the :meth:`toolbox.clone` method and then mated using the
    :meth:`toolbox.mate` method. Only the first child is appended to the
    offspring population :math:`P_\mathrm{o}`, the second child is discarded.
    In the case of a mutation, one individual is selected at random from
    :math:`P_\mathrm{p}`, it is cloned and then mutated using using the
    :meth:`toolbox.mutate` method. The resulting mutant is appended to
    :math:`P_\mathrm{o}`. In the case of a reproduction, one individual is
    selected at random from :math:`P_\mathrm{p}`, cloned and appended to
    :math:`P_\mathrm{o}`.

    This variation is named *Or* because an offspring will never result from
    both operations crossover and mutation. The sum of both probabilities
    shall be in :math:`[0, 1]`, the reproduction probability is
    1 - *cxpb* - *mutpb*.
    """
    assert (cxpb + mutpb) <= 1.0, (
        "The sum of the crossover and mutation probabilities must be smaller "
        "or equal to 1.0.")

    offspring = []
    for _ in range(lambda_):
        op_choice = random.random()
        if op_choice < cxpb:            # Apply crossover
            ind1, ind2 = list(map(toolbox.clone, random.sample(population, 2)))
            ind1, ind2 = toolbox.mate(ind1, ind2)
            del ind1.fitness.values
            offspring.append(ind1)
        elif op_choice < cxpb + mutpb:  # Apply mutation
            ind = toolbox.clone(random.choice(population))
            ind, = toolbox.mutate(ind)
            del ind.fitness.values
            offspring.append(ind)
        else:                           # Apply reproduction
            offspring.append(random.choice(population))

    return offspring
def CheckPoint(newCheckpoint):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if (file.endswith('.pkl')==True)and(file==newCheckpoint):
                checkpoint=True
                break
            elif(file.endswith('.pkl')==True)and(file!=newCheckpoint):
                checkpoint=None
            else:
                checkpoint=None
        break
    return checkpoint
def eaSimpleModWithElitism(dir,dirChkP,population, toolbox, cxpb, mutpb, ngen, nrun, FREQ, stats=None,
             halloffame=None, checkpoint=None, verbose=__debug__):
    """This algorithm is similar to DEAP eaSimple() algorithm, with the modification that
    halloffame is used to implement an elitism mechanism. The individuals contained in the
    halloffame are directly injected into the next generation and are not subject to the
    genetic operators of selection, crossover and mutation.
    Although, we add some new features:
    -> Create Gen files saving the Individual generated from start.
    -> Add some checkpoint for restart the evolution from a previos state.
    -> Add a Command log updating function(this is a third party code part, credits for she/he), for tracking run status.
    -> Save logbook from start, before was saved at end.
    -> Add some memory status and fitness tracking for files.
    """
    File2HoF=str(dir+'HOFPoP.txt')
    counter=0
    start_gen = 0
    #sys.stdout.write(dir_path+'/'+dir)
    if checkpoint:
        # A file name has been given, then load the data from the file
        cp = pickle.load(open(dirChkP, "rb"))
        sys.stdout.write("\n")
        sys.stdout.write('Archivo detectado: /'+str(dirChkP))
        sys.stdout.write("\n")
        sys.stdout.flush()
        population = cp["population"]
        start_gen = cp["generation"]
        halloffame = cp["halloffame"]
        logbook = cp["logbook"]
        random.setstate(cp["rndstate"])
        #sys.stdout.write(str(start_gen))
        if start_gen>=ngen-1:
            sys.stdout.write("\n")
            sys.stdout.write("Evolución Completa de la corrida "+str(nrun)+ ": Cambiar número de corrida")
            sys.stdout.write("\n")
            sys.stdout.flush()
            input("Press Enter to continue...")
            sys.exit()
            #break
    else:
        # Start a new evolution
        tracemalloc.start()
        sys.stdout.write("\n")
        sys.stdout.write("Creando nueva evolucion")
        sys.stdout.write("\n")
        sys.stdout.flush()
        logbook = tools.Logbook()
        logbook.header = ['gen', 'nevals'] + (stats.fields if stats else [])
        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in population if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        FILEHOF=open(File2HoF,'a')
        File2Gena=str(dir+'GENPoPBase.txt')
        #FILEGEN=open(File2Gen,'a')
        for ind, fit in zip(invalid_ind, fitnesses):
            FILEGEN=open(File2Gena,'a')
            ind.fitness.values = fit
            current, peak = tracemalloc.get_traced_memory()
            strpop=str(population[counter])
            strfit=str(population[counter].fitness.values[0])
            FILEGEN.write(f"{counter};"+f"{strpop};"+f"{strfit};"+f" Current memory: {current / 10**4}MB; Peak: {peak / 10**4}MB;\n")
            FILEGEN.write('\n')
            FILEGEN.close()
            counter=counter+1
        #FILEGEN.close()
        if halloffame is None:
            raise ValueError("halloffame parameter must not be empty!")
        halloffame.update(population)
        #Saving data to file by the best individual
        FILEHOF.write(str(halloffame.items[0])+"; "+str(halloffame.items[0].fitness.values[0]))
        FILEHOF.write('\n')
        FILEHOF.close()
        record = stats.compile(population) if stats else {}
        logbook.record(gen=start_gen, nevals=len(invalid_ind), **record)
        if verbose:
            sys.stdout.write("\n")
            #sys.stdout.write(logbook.stream)
            sys.stdout.flush()
            #print(logbook.stream)
        update_progress("Corriendo GP -...", 0/3)
        sys.stdout.flush()
        #Saving the generation 0
        #for m in range(len(population)):
        #    current, peak = tracemalloc.get_traced_memory()
        #    FILEGEN.write(str(population[m])+"; "+str(population[m].fitness.values[0])+f"; Current memory: {current / 10**4}MB; Peak: {peak / 10**4}MB;\n")
        #    FILEGEN.write('\n')
        tracemalloc.stop()
    # Begin the generational process   
    #Naming the best individual for generation data file
    hof_size = len(halloffame.items) if halloffame.items else 0
    tracemalloc.start()
    for gen in range(start_gen, ngen + 1):
        current, peak = tracemalloc.get_traced_memory()
        # Select the next generation individuals
        offspring = toolbox.select(population, len(population) - hof_size)
        # Vary the pool of individuals
        offspring = varAnd(offspring, toolbox, cxpb, mutpb)
        update_progress("Corriendo GP - Gen:"+str(gen)+"/"+str(ngen)+" Individuo-> "+str(halloffame.items[0])+" Desempeño-> "+str(halloffame.items[0].fitness.values[0]), (gen)/ngen)
        #sys.stdout.write(f"\nCurrent memory usage is {current / 10**4}MB; Peak was {peak / 10**4}MB\n")
        #update_progress("Corriendo GP - Gen:"+str(gen)+"/"+str(ngen)+" Individuo-> "+str(offspring), (gen)/ngen)
        sys.stdout.flush()
        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        #Saving the generation
        File2Gen=str(dir+'GENPoP-'+str(gen)+'.txt')
        counter=0
        for ind, fit in zip(invalid_ind, fitnesses):
            FILE2GEN=open(File2Gen,'a')
            ind.fitness.values = fit
            current, peak = tracemalloc.get_traced_memory()
            strpop=str(offspring[counter])
            strfit=str(offspring[counter].fitness.values[0])
            FILE2GEN.write(f"{counter};"+f"{strpop};"+f"{strfit};"+f" Current memory: {current / 10**4}MB; Peak: {peak / 10**4}MB;\n")
            FILE2GEN.write('\n')
            FILE2GEN.close()
            counter=counter+1
        # add the best back to population:
        offspring.extend(halloffame.items)
        # Update the hall of fame with the generated individuals
        halloffame.update(offspring)
        #Saving data to file by the best individual
        FILEHOF=open(File2HoF,'a')
        FILEHOF.write(str(halloffame.items[0])+"; "+str(halloffame.items[0].fitness.values[0]))
        FILEHOF.write('\n')
        FILEHOF.close()
        # Replace the current population by the offspring
        population[:] = offspring
        # Append the current generation statistics to the logbook
        record = stats.compile(population) if stats else {}
        logbook.record(gen=gen, nevals=len(invalid_ind), **record)
        population = toolbox.select(population, k=len(population))
        auxOffspring=str(offspring)
        #for m in range(len(offspring)):
        #    FILEGEN.write(str(offspring[m])+"; "+str(offspring[m].fitness.values[0])+f"; Current memory: {current / 10**4}MB; Peak: {peak / 10**4}MB;\n")
        #    FILEGEN.write('\n')          
        if gen % FREQ == 0:
            sys.stdout.write(str(gen % FREQ)) 
            # Fill the dictionary using the dict(key=value[, ...]) constructor
            #sys.stdout.write(str(offspring))
            cp = dict(population=population, generation=gen, halloffame=halloffame,
                    logbook=logbook, rndstate=random.getstate())
            #cp = dict(population=str(offspring[m]))
            pickle.dump(cp, open(dirChkP, "wb"))   
        if verbose:
            sys.stdout.write("\n")
            #Saving statistics
            MyFile=str(dir+'Statistics.txt')
            MyOutFile=open(MyFile, 'a')
            MyOutFile.write(str(logbook.stream))
            MyOutFile.write("\n")
            sys.stdout.flush()
            MyOutFile.close()
        #FILEGEN.close()
        #FILE2GEN.close()
    tracemalloc.stop()
    update_progress("Corriendo GP - Gen:"+str(gen)+"/"+str(ngen), 1)
    sys.stdout.flush()
    return population, logbook
