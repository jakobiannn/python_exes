from sudoku import state_sudoku, fair_evaluator
from asearch import a_search
from timeit import Timer

initial = state_sudoku()


def goal(initial):
    for row in initial.table:
        for col in row:
            if col == 0:
                return False
    return True


print('fair =', fair_evaluator(initial))

f = lambda: a_search(initial, goal, fair_evaluator)


res = f()
print('has decision  :', res['solved'])
print('open states   :', res['openstates'])
print('closed states :', res['closedstates'])
print('result path   :')
for m in res['path']:
    print(m)

t = Timer(f)
print("Time = ", t.timeit(number=1))
