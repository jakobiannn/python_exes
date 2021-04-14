import random
from copy import deepcopy

field = [
    [0, 3, 0, 2, 0, 7, 0, 9, 0],
    [0, 0, 0, 0, 9, 3, 0, 7, 0],
    [7, 5, 0, 0, 6, 8, 1, 0, 3],
    [0, 7, 0, 3, 0, 6, 9, 0, 5],
    [9, 1, 0, 0, 0, 2, 8, 0, 0],
    [0, 0, 5, 7, 8, 0, 0, 0, 1],
    [0, 0, 3, 9, 0, 1, 0, 0, 6],
    [0, 0, 0, 6, 0, 4, 3, 0, 0],
    [6, 0, 0, 8, 3, 5, 4, 0, 2]
]
field1 = [
    [1, 3, 4, 2, 5, 7, 6, 9, 8],
    [0, 6, 0, 1, 9, 3, 5, 7, 4],
    [7, 5, 9, 4, 6, 8, 1, 2, 3],
    [0, 7, 0, 3, 1, 6, 9, 4, 5],
    [9, 1, 6, 5, 4, 2, 8, 3, 7],
    [3, 4, 5, 7, 8, 9, 2, 6, 1],
    [4, 8, 3, 9, 2, 1, 7, 5, 6],
    [5, 2, 1, 6, 7, 4, 3, 8, 9],
    [6, 9, 7, 8, 3, 5, 4, 1, 2]
]


class state_windoku():

    def __init__(self, parent=None, data=None, depth=0):
        """ Generation of the base table """
        self._depth = depth
        self.parent = parent
        if data is not None:
            self.table = data
        else:
            self.table = field1

    def __hash__(self):
        hash = ""
        for row in range(9):
            for col in range(9):
                hash += str(self.table[row][col])
        return int(hash)

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def show(self):
        for row in self.table:
            print(row)

    @staticmethod
    def get_second_range(item):
        if 1 <= item < 4:
            return range(1, 4)
        elif 5 <= item < 8:
            return range(5, 8)
        return None

    @staticmethod
    def get_range(item):
        if 0 <= item < 3:
            return range(0, 3)
        elif 3 <= item < 6:
            return range(3, 6)
        else:
            return range(6, 9)

    def check_second_square(self, value, row, col):
        if self.get_second_range(row) is not None and \
                self.get_second_range(col) is not None:
            for cell_row in self.get_second_range(row):
                for cell_col in self.get_second_range(col):
                    if self.table[cell_row][cell_col] == value:
                        return False
        return True

    def check_square(self, value, row, col):
        for cell_row in self.get_range(row):
            for cell_col in self.get_range(col):
                if self.table[cell_row][cell_col] == value:
                    return False
        return True

    def is_append(self, coord, num):
        row, col = coord
        if num in self.table[row]:
            return False
        for row_num in range(9):
            if self.table[row_num][col] == num:
                return False
        if not self.check_square(num, row, col):
            return False
        if not self.check_second_square(num, row, col):
            return False
        return True

    def get_moves(self):
        moves = []
        for row in range(9):
            for col in range(9):
                if self.table[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_append((row, col), num):
                            new_table = deepcopy(self.table)
                            new_table[row][col] = num
                            moves.append(state_windoku(self, new_table, self._depth + 1))
        return moves
# сумма незаполненных ячеек на поле
def fair_evaluator(state):
    count = 0
    for row in state.table:
        for col in row:
            if col == 0:
                count += 1
    return count
