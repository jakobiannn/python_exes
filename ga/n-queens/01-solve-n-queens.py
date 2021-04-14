from deap import base
from deap import creator
from deap import tools

import random
import array

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import elitism
import queens

# Количество ферзей:
NUM_OF_QUEENS = 8

# Ограничение популяции:
POPULATION_SIZE = 300
# Ограничение популяции:максимальное число генераций
MAX_GENERATIONS = 100
#количество подходящих результатов
HALL_OF_FAME_SIZE = 30
P_CROSSOVER = 0.9  # Вероятность кроссинговера
P_MUTATION = 0.1   # Вероятность мутации

# установка random для повторяющихся результатов
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# create the desired N-
nQueens = queens.NQueensProblem(NUM_OF_QUEENS)

toolbox = base.Toolbox()

# определение минимизирующей фитнес стратегии:
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

# Создание класса на основе списка целых чисел Individual:
creator.create("Individual", array.array, typecode='i', fitness=creator.FitnessMin)

# создание оператора генерирующего случайные индексы:
toolbox.register("randomOrder", random.sample, range(len(nQueens)), len(nQueens))

# создание класса IndvidualCreator для заполнения Individual случайными индексами:
toolbox.register("individualCreator", tools.initIterate, creator.Individual, toolbox.randomOrder)

#Создание класса составления популяции:
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)


# вычисление количества нарушений:
def getViolationsCount(individual):
    return nQueens.getViolationsCount(individual),  


toolbox.register("evaluate", getViolationsCount)


# Регистрация стандартных генетических операторов:
toolbox.register("select", tools.selTournament, tournsize=2)
toolbox.register("mate", tools.cxUniformPartialyMatched, indpb=2.0/len(nQueens))
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=1.0/len(nQueens))


def main():

    #создание начальной популяции:
    population = toolbox.populationCreator(n=POPULATION_SIZE)

    # prepare the statistics object:
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)
    stats.register("avg", np.mean)

    # создания объекта решений:
    hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

    # реение задачи генетическим алгоритмом с использованием критерия элитраности:
    population, logbook = elitism.eaSimpleWithElitism(population, toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTATION,
                                              ngen=MAX_GENERATIONS, stats=stats, halloffame=hof, verbose=True)

    # выписка информации о решениях:
    print("- Best solutions are:")
    for i in range(HALL_OF_FAME_SIZE):
        print(i, ": ", hof.items[i].fitness.values[0], " -> ", hof.items[i])

    # вывод статистики в графическом виде:
    minFitnessValues, meanFitnessValues = logbook.select("min", "avg")
    plt.figure(1)
    sns.set_style("whitegrid")
    plt.plot(minFitnessValues, color='red')
    plt.plot(meanFitnessValues, color='green')
    plt.xlabel('Generation')
    plt.ylabel('Min / Average Fitness')
    plt.title('Min and Average fitness over Generations')

    # демонстрация лучшего решения на доске:
    sns.set_style("whitegrid", {'axes.grid' : False})

    # демонстрация графика:
    plt.show()


if __name__ == "__main__":
    main()
