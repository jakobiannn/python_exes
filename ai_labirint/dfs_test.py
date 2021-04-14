from labirint import labirint
from dfs import *
from timeit import Timer

initial = labirint()

field1 = [
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 0, 0, 'X'],
    ['W', 'W', 0, 'W', 'W'],
    [0, 0, 0, 0, 'W'],
    ['W', 0, 'W', 0, 'W'],
]
goal = labirint(None, field1)

print(f"Initial state: {initial}")
initial.show()
f = lambda: dfs(initial, goal, 20)

res = f()
print('has decision  :', res[0])
print('open states   :', res[2])
print('closed states :', res[3])
print('result path   :')
for m in res[1]:
    print(m.field)

t = Timer(f)
print("Time = ", t.timeit(number=1))
