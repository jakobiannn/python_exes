from copy import deepcopy

from base import base_state
import random

#field[0] - 5L 
#field[1] - 3L
field = [0, 0]

class state_buckets(base_state):
    def __init__(self, parent=None, initial=None, depth=0):
        self._depth = depth
        self.parent = parent
        if initial is not None:
            self.field = initial
        else:
            self.field = field

    def __hash__(self):
        hash_num = ""
        for bucket in self.field:
            hash_num += str(bucket)
        return int(hash_num)

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def show(self):
        for row in self.field:
            print(row)
        print('---------------------')


    def get_moves(self):
        moves = []
        new_table = deepcopy(self.field)

        new_table[0] = 5
        moves.append(state_buckets(self, new_table, self._depth + 1))
        new_table = deepcopy(self.field)

        new_table[1] = 3
        moves.append(state_buckets(self, new_table, self._depth + 1))
        new_table = deepcopy(self.field)

        new_table[0] = 0
        moves.append(state_buckets(self, new_table, self._depth + 1))
        new_table = deepcopy(self.field)

        new_table[1] = 0
        moves.append(state_buckets(self, new_table, self._depth + 1))
        new_table = deepcopy(self.field)

        while new_table[0] != 5 and new_table[1] != 0:
            new_table[0] += 1
            new_table[1] -= 1
        moves.append(state_buckets(self, new_table, self._depth + 1))
        new_table = deepcopy(self.field)

        while new_table[1] != 3 and new_table[0] != 0:
            new_table[0] -= 1
            new_table[1] += 1
        moves.append(state_buckets(self, new_table, self._depth + 1))
        new_table = deepcopy(self.field)
        return moves

def fair_evaluator(initial, goal):
	return min(abs(4 - initial.field[0]), abs(4 - initial.field[0]))

s = state_buckets()
for m in s.get_moves():
    print(m.field)