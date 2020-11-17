from sudoku import state_sudoku
from bfs import *
from timeit import Timer

count_state = state_sudoku()

initial = count_state
def goal(state):
    for row in state.table:
        for col in row:
            if col == 0:
                return False
    return True

print(initial)

f = lambda: bfs(initial, goal)

res = f()
print('has decision  :', res[0])
print('open states   :', res[2])
print('closed states :', res[3])
print('result path   :')
for m in res[1]:
    print(m)

t = Timer(f)
print("Time = ", t.timeit(number=100))
