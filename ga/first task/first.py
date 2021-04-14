from deap import base
from deap import creator
from deap import tools
import math
from deap import algorithms
import random
import numpy
import matplotlib.pyplot as plt
import seaborn as sns

# problem constants:
# точность до 4 знаков
ONE_MAX_LENGTH = 17  # length of bit string to be optimized
MAX_VALUE = (2 ** ONE_MAX_LENGTH) - 1 
PRECISION = 0.000000000001
MAX_FITNESS_VALUE = 100
# Genetic Algorithm constants:
POPULATION_SIZE = 200
P_CROSSOVER = 0.9 
P_MUTATION = 0.1   
MAX_GENERATIONS = 30
LEFT_BORDER = -9
RIGHT_BORDER = 9


def function(t):
    return (1.1*t - 1.7)* math.cos(math.pi * t + 1.5)



# set the random seed:
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

toolbox = base.Toolbox()
  

# create an operator that randomly returns 0 or 1:
toolbox.register("zeroOrOne", random.randint, 0, 1)

# define a single objective, maximizing fitness strategy:
creator.create("FitnessMax", base.Fitness, weights=(1.0,))

# create the Individual class based on list:
creator.create("Individual", list, fitness=creator.FitnessMax)

# create the individual operator to fill up an Individual instance:
toolbox.register("individualCreator", tools.initRepeat, creator.Individual, toolbox.zeroOrOne, ONE_MAX_LENGTH)

# create the population operator to generate a list of individuals:
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)


# fitness calculation:
# compute the number of '1's in the individual
def fitness(individual):
    value = findX(individual)
    diffferncial = abs((function(value + PRECISION) - function(value)) / PRECISION)
    return MAX_FITNESS_VALUE - diffferncial,  # return a tuple

def findX(individual):
    number = 0
    for i in range(ONE_MAX_LENGTH):
        number += individual[i] * (2 ** (ONE_MAX_LENGTH - i - 1))
    return  LEFT_BORDER + (number / MAX_VALUE)*(RIGHT_BORDER - LEFT_BORDER)
    

toolbox.register("evaluate", fitness)


toolbox.register("select", tools.selTournament, tournsize=3)


toolbox.register("mate", tools.cxOnePoint)


toolbox.register("mutate", tools.mutFlipBit, indpb=1.0/ONE_MAX_LENGTH)


def main():

    # Создание начальной популяции:
    population = toolbox.populationCreator(n=POPULATION_SIZE)

    # Создание статистического объекта
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("max", numpy.max)
    stats.register("avg", numpy.mean)

    # выполнение алгоритма:
    population, logbook = algorithms.eaSimple(population, toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTATION, ngen=MAX_GENERATIONS,
                                   stats=stats, verbose=True)
    print('Значение фитнес функции')
    print(fitness(population[0]))
    print('требуемая популяция')
    print(population[0])
    print(findX(population[0]))
    value = function(findX(population[0]))
    print('Значение функции')
    print(value)

    # Genetic Algorithm is done - extract statistics:
    maxFitnessValues, meanFitnessValues = logbook.select("max", "avg")

    # plot statistics:
    sns.set_style("whitegrid")
    plt.plot(maxFitnessValues, color='red')
    plt.plot(meanFitnessValues, color='green')
    plt.xlabel('Generation')
    plt.ylabel('Max / Average Fitness')
    plt.title('Max and Average Fitness over Generations')
    plt.show()


if __name__ == "__main__":
    main()