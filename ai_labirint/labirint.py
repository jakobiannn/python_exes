from copy import deepcopy
import math
from base import base_state

field = [
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 0, 0, 0],
    ['W', 'W', 0, 'W', 'W'],
    ['X', 0, 0, 0, 'W'],
    ['W', 0, 'W', 0, 'W'],
]

class labirint(base_state):

    def __init__(self, parent=None, data=None, depth=0):
        self._depth = depth
        self.parent = parent
        if data is not None:
            self.field = data
        else:
            self.field = field

    def __hash__(self):
        hash = ""
        for row in range(5):
            for col in range(5):
                if self.field[row][col] == 'W':
                    hash += '1'
                elif self.field[row][col] == 'X':
                    hash += '2'
                else:
                    hash += str(self.field[row][col])
        return int(hash)

    def show(self):
        for row in self.field:
            print(row)

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def check_n_append(self, coord, check_coord, moves):
        old_row, old_col = coord
        row, col = check_coord
        if row <= 4 and col <= 4:
            if self.field[row][col] == 0:
                new_table = deepcopy(self.field)
                new_table[old_row][old_col] = 0
                new_table[row][col] = 'X'
                moves.append(labirint(self, new_table, self._depth + 1))

    def get_moves(self):
        moves = []
        for row in range(5):
            for col in range(5):
                if self.field[row][col] == 'X':
                    self.check_n_append((row, col), (row + 1, col), moves)
                    self.check_n_append((row, col), (row - 1, col), moves)
                    self.check_n_append((row, col), (row, col + 1), moves)
                    self.check_n_append((row, col), (row, col - 1), moves)
        return moves


# возвратим отрицательную длину вектора (т.к. чем меньше длина, тем лучше)
# от текущего положения и целевого
def fair_evaluator(initial, goal):
    for row in range(5):
        for col in range(5):
            if initial.field[row][col] == 'X':
                init_x, init_y = row, col
            if goal.field[row][col] == 'X':
                goal_x, goal_y = row, col
    return (-1) * math.sqrt((goal_x - init_x) ** 2 + (goal_y - init_y) ** 2)
