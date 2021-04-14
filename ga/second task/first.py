from deap import base
from deap import creator
from deap import tools
import math
from deap import algorithms
import random
import numpy
import matplotlib.pyplot as plt
import seaborn as sns
import time

# problem constants:
# точность до 4 знаков
ONE_MAX_LENGTH = 2  # length of bit string to be optimized
MAX_VALUE = (2 ** ONE_MAX_LENGTH) - 1 
PRECISION = 0.000000000001
MAX_FITNESS_VALUE = 10000000
# Genetic Algorithm constants:
POPULATION_SIZE = 200
P_CROSSOVER = 0.9 
P_MUTATION = 0.1   
MAX_GENERATIONS = 30
LEFT_BORDER = -9
RIGHT_BORDER = 9


def func(x,y):
    firstPart = 1+((x + y + 1)**2)*(19-14*x+3*x**2-14*y+6*x*y + 3*y**2)
    secondPart = 30+((2*x-3*y)**2)*(18-32*x+12*x**2+48*y-36*x*y+27*y**2)
    return firstPart * secondPart



# set the random seed:
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

toolbox = base.Toolbox()

def decRandom():
    return random.random() * 4 - 2
  

# create an operator that randomly returns 0 or 1:
toolbox.register("zeroOrOne", decRandom)

# define a single objective, maximizing fitness strategy:
creator.create("FitnessMax", base.Fitness, weights=(-1.0,))

# create the Individual class based on list:
creator.create("Individual", list, fitness=creator.FitnessMax)

# create the individual operator to fill up an Individual instance:
toolbox.register("individualCreator", tools.initRepeat, creator.Individual, toolbox.zeroOrOne, ONE_MAX_LENGTH)

# create the population operator to generate a list of individuals:
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)


# fitness calculation:
# compute the number of '1's in the individual
def fitness(individual):
    #time.sleep(1)
    return func(individual[0],individual[1]),  # return a tuple

    

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
    print(func(population[0][0],population[0][1]))

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