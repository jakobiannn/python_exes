from hanoitower import state_hanoi
from bfs import *
from timeit import Timer

goal1 = [
    [],
    [],
    [3, 2, 1]
]

goal2 = [
    [],
    [3, 2, 1],
    []
]

initial = state_hanoi()


def goal(state):
    if state.field == goal1 or state.field == goal2:
        return True
    return False


print(initial.field)
f = lambda: bfs(initial, goal)

res = f()
print('has decision  :', res[0])
print('open states   :', res[2])
print('closed states :', res[3])
print('result path   :')
for m in res[1]:
    print(m.field)

t = Timer(f)
print("Time = ", t.timeit(number=100))
