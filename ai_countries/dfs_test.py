from countries import state_countries
from dfs import *
from timeit import Timer

initial = state_countries()
def goal(state):
    for key in state.boards:
        if state.boards[key] is None:
            return False
    return True

print(f"Initial state: {initial.boards}")

f = lambda: dfs(initial, goal, 100)

res = f()
print('has decision  :', res[0])
print('open states   :', res[2])
print('closed states :', res[3])
print('result path   :')
for m in res[1]:
    print(m.boards)

t = Timer(f)
print("Time = ", t.timeit(number=1))
