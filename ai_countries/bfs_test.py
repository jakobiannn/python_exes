from countries import state_countries
from bfs import *
from timeit import Timer
# boards = {
# 	'К': ['П', 'Р', 'Ф'],
# 	'П': ['К', 'Р'],
# 	'Р': ['К', 'Ф', 'П'],
# 	'Ф': ['К', 'Р']
# }
# countries_colours = {
# 	'К': 'red',
# 	'П': 'white',
# 	'Р': None,
# 	'Ф': 'white'
# }
def goal(state):
    for key in state.boards:
        if state.boards[key] is None:
            return False
    return True

initial = state_countries()

print(initial)

f = lambda: bfs(initial, goal)

res = f()
print('has decision  :', res[0])
print('open states   :', res[2])
print('closed states :', res[3])
print('result path   :')
for m in res[1]:
    print(m.boards)

t = Timer(f)
print("Time = ", t.timeit(number=100))
