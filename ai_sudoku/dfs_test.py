from sudoku import state_sudoku
from dfs import *
from timeit import Timer

initial = state_sudoku()
def goal(state):
    for row in state.table:
        for col in row:
            if col == 0:
                return False
    return True

print(f"Initial state: {initial}")

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