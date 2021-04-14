from hitori import state_hitori
from dfs import *
from timeit import Timer

initial = state_hitori()


def goal(state):
    if len(state.get_moves()) == 0:
        return True
    return False


print(f"Initial state: {initial}")
initial.show()
f = lambda: dfs(initial, goal, 20)

res = f()
print('has decision  :', res[0])
print('open states   :', res[2])
print('closed states :', res[3])
print('result path   :')
for m in res[1]:
    print(m)

t = Timer(f)
print("Time = ", t.timeit(number=1))
