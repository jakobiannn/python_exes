from labirint import fair_evaluator
from labirint import labirint
from asearch import a_search
from timeit import Timer

initial = labirint()

field = [
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 0, 0, 'X'],
    ['W', 'W', 0, 'W', 'W'],
    [0, 0, 0, 0, 'W'],
    ['W', 0, 'W', 0, 'W'],
]
goal = labirint(field)

print('fair =', fair_evaluator(initial, goal))
print('good =', good_evaluator(initial, goal))
print('weak =', weak_evaluator(initial, goal))
# print('bad  =', bad_evaluator(initial, goal))

f = lambda: a_search(initial, goal, fair_evaluator)
# f = lambda: a_search(initial, goal, good_evaluator)
# f = lambda: a_search(initial, goal, weak_evaluator)
# f = lambda: a_search(initial, goal, bad_evaluator)

res = f()
print('has decision  :', res['solved'])
print('open states   :', res['openstates'])
print('closed states :', res['closedstates'])
print('result path   :')
for m in res['path']:
    print(m)

t = Timer(f)
print("Time = ", t.timeit(number=1))
