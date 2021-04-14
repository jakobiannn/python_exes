from deap import tools
from deap import algorithms

def eaSimpleWithElitism(population, toolbox, cxpb, mutpb, ngen, stats=None,
             halloffame=None, verbose=__debug__):
  
    #подготовка исходных данных для генерации
    logbook = tools.Logbook()
    logbook.header = ['gen', 'nevals'] + (stats.fields if stats else [])
   # сравнение единиц с не валидным фитнес значением
    invalid_ind = [ind for ind in population if not ind.fitness.valid]
    fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    if halloffame is None:
        raise ValueError("halloffame parameter must not be empty!")

    halloffame.update(population)
    hof_size = len(halloffame.items) if halloffame.items else 0

    record = stats.compile(population) if stats else {}
    logbook.record(gen=0, nevals=len(invalid_ind), **record)
    if verbose:
        print(logbook.stream)

    # Начало процесса генерации
    for gen in range(1, ngen + 1):

        # выборка следующего поколения единиц
        offspring = toolbox.select(population, len(population) - hof_size)

        #отклонение поколения
        offspring = algorithms.varAnd(offspring, toolbox, cxpb, mutpb)

        # сравнение единиц с не валидным фитнес значением
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # возвращение лучшего значения популяции
        offspring.extend(halloffame.items)

        # дополненией результата новым поколением
        halloffame.update(offspring)

        #замещение старой популяции новой
        population[:] = offspring

        # обновление и вывод статистики
        record = stats.compile(population) if stats else {}
        logbook.record(gen=gen, nevals=len(invalid_ind), **record)
        if verbose:
            print(logbook.stream)

    return population, logbook

