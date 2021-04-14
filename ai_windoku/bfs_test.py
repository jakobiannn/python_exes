from windoku import state_windoku
from bfs import *
from timeit import Timer

initial = state_windoku()


def goal(state):
    if len(state.get_moves()) == 0:
        return True
    return False


print(initial)
initial.show()
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
