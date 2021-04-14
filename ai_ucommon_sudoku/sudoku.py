import random
from copy import deepcopy

from pip._vendor.urllib3.connectionpool import xrange
field = [
[1, 2, 3, 7, 8, 9],
[4, 5, 6, 1, 2, 3],
[7, 8, 9, 4, 5, 6],
[2, 3, 4, 8, 9, 1],
[5, 6, 7, 2, 3, 4],
[8, 9, 1, 5, 6, 7],
]

zfield = [
[3, 2, 5, 4, 6, 1],
[6, 1, 4, 3, 2, 5],
[4, 5, 1, 2, 3, 0],
[2, 0, 3, 1, 5, 0],
[1, 3, 6, 5, 4, 2],
[5, 4, 2, 6, 1, 3],
]

class state_sudoku:

    def __init__(self, parent=None, data=None, depth=0, n=3):
        """ Generation of the base table """
        self.n = n
        self._depth = depth
        self.parent = parent
        if data is not None:
            self.table = data
        else:
            self.table = zfield

    def __hash__(self):
        hash = ""
        for row in range(6):
            for col in range(6):
                hash += str(self.table[row][col])
        return int(hash)

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def show(self):
        for row in self.table:
            print(row)

    @staticmethod
    def get_row_range(item):
        if 0 <= item < 3:
            return range(0, 3)
        elif 3 <= item < 6:
            return range(3, 6)
        else:
            return range(6, 9)

    @staticmethod
    def get_col_range(item):
        if 0 <= item < 2:
            return range(0, 2)
        elif 2 <= item < 4:
            return range(2, 4)
        else:
            return range(4, 6)

    def check_square(self, value, row, col):
        for cell_row in self.get_row_range(row):
            for cell_col in self.get_col_range(col):
                if self.table[cell_row][cell_col] == value:
                    return False
        return True

    def is_append(self, coord, num):
        row, col = coord
        if num in self.table[row]:
            return False
        for row_num in range(6):
            if self.table[row_num][col] == num:
                return False
        if not self.check_square(num, row, col):
            return False
        return True

    def get_moves(self):
        moves = []
        for row in range(6):
            for col in range(6):
                if self.table[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_append((row, col), num):
                            new_table = deepcopy(self.table)
                            new_table[row][col] = num
                            moves.append(state_sudoku(self, new_table, self._depth + 1))
        return moves


# сумма незаполненных ячеек на поле
def fair_evaluator(state):
    count = 0
    for row in state.table:
        for col in row:
            if col == 0:
                count += 1
    return count
