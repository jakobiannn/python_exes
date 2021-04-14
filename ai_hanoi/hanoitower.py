from copy import deepcopy

from base import base_state
import random

towers = [
    [3, 2, 1],
    [],
    []
]


class state_hanoi(base_state):
    def __init__(self, parent=None, initial=None, depth=0):
        self._depth = depth
        self.parent = parent
        if initial is not None:
            self.field = initial
        else:
            self.field = towers

    def __hash__(self):
        hash_num = ""
        for row in self.field:
            if len(row) == 0:
                hash_num += '4'
            for col in row:
                hash_num += str(col)
        return int(hash_num)

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def check_towers(self, field, moves):
        for i in range(3):
            for j in range(3):
                if len(field[i]) > 0 and len(field[j]) > 0:
                    if field[i][len(field[i]) - 1] < field[j][len(field[j]) - 1]:
                        copy_field = deepcopy(field)
                        block = copy_field[i].pop()
                        copy_field[j].append(block)
                        moves.append(state_hanoi(self, copy_field, self._depth + 1))
                elif len(field[i]) > 0 and len(field[j]) == 0:
                    copy_field = deepcopy(field)
                    block = copy_field[i].pop()
                    copy_field[j].append(block)
                    moves.append(state_hanoi(self, copy_field, self._depth + 1))

    def get_moves(self):
        moves = []
        self.check_towers(self.field, moves)
        return moves

def fair_evaluator(initial, goal):
    return 3 - max(len(initial.field[0]), len(initial.field[1]), len(initial.field[2]))

s = state_hanoi()

for m in s.get_moves():
    print(m.__hash__())