from buckets import state_buckets
from bfs import *
from timeit import Timer

initial = state_buckets()


def goal(state):
    for bucket in state.field:
        if bucket == 4:
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
    print(m.field)

t = Timer(f)
print("Time = ", t.timeit(number=100))
