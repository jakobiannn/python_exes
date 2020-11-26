import random
from copy import deepcopy

import solver
from pip._vendor.urllib3.connectionpool import xrange
field = [
[1, 2, 3, 7, 8, 9, 4, 5, 6],
[4, 5, 6, 1, 2, 3, 7, 8, 9],
[7, 8, 9, 4, 5, 6, 1, 2, 3],
[2, 3, 4, 8, 9, 1, 5, 6, 7],
[5, 6, 7, 2, 3, 4, 8, 9, 1],
[8, 9, 1, 5, 6, 7, 2, 3, 4],
[3, 4, 5, 9, 1, 2, 6, 7, 8],
[6, 7, 8, 3, 4, 5, 9, 1, 2],
[9, 1, 2, 6, 7, 8, 3, 4, 5]
]

zfield = [
[1, 2, 3, 0, 8, 9, 4, 5, 6],
[4, 5, 0, 1, 2, 0, 7, 8, 9],
[7, 8, 9, 4, 5, 6, 1, 0, 3],
[2, 3, 4, 0, 9, 0, 5, 6, 0],
[5, 0, 7, 2, 3, 4, 8, 9, 1],
[8, 9, 1, 5, 6, 7, 2, 3, 4],
[3, 4, 5, 0, 1, 2, 0, 7, 8],
[6, 7, 8, 3, 4, 5, 9, 1, 2],
[9, 1, 2, 6, 7, 8, 0, 4, 5]
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
            self.table = [[int((i * n + i / n + j) % (n * n) + 1) for j in range(n * n)] for i in range(n * n)]
            self.generate_full_field()

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

    def transposing(self):
        """ Transposing the whole grid """
        self.table = map(list, zip(*self.table))
        self.table = list(self.table)

    def swap_rows_small(self):
        """ Swap the two rows """
        area = random.randrange(0, self.n, 1)
        line1 = random.randrange(0, self.n, 1)
        # получение случайного района и случайной строки
        N1 = area * self.n + line1
        # номер 1 строки для обмена

        line2 = random.randrange(0, self.n, 1)
        # случайная строка, но не та же самая
        while line1 == line2:
            line2 = random.randrange(0, self.n, 1)

        N2 = area * self.n + line2
        # номер 2 строки для обмена

        self.table[N1], self.table[N2] = self.table[N2], self.table[N1]

    def swap_colums_small(self):
        state_sudoku.transposing(self)
        state_sudoku.swap_rows_small(self)
        state_sudoku.transposing(self)

    def swap_rows_area(self):
        """ Swap the two area horizon """
        area1 = random.randrange(0, self.n, 1)
        # получение случайного района

        area2 = random.randrange(0, self.n, 1)
        # ещё район, но не такой же самый
        while area1 == area2:
            area2 = random.randrange(0, self.n, 1)

        for i in range(0, self.n):
            N1, N2 = area1 * self.n + i, area2 * self.n + i
            self.table[N1], self.table[N2] = self.table[N2], self.table[N1]

    def swap_colums_area(self):
        state_sudoku.transposing(self)
        state_sudoku.swap_rows_area(self)
        state_sudoku.transposing(self)

    def generate_full_field(self, amt=10):
        '''mix_func = ['self.transposing()',
                    'self.swap_rows_small()',
                    'self.swap_colums_small()',
                    'self.swap_rows_area()',
                    'self.swap_colums_area()']
        for _ in xrange(1, amt):
            id_func = random.randrange(0, len(mix_func), 1)
            eval(mix_func[id_func])'''
        flook = [[0 for j in range(self.n * self.n)] for i in range(self.n * self.n)]
        iterator = 0
        difficult = self.n ** 4  # Первоначально все элементы на месте
        print("---------------------------")
        self.show()
        print("---------------------------")

        while iterator < self.n ** 4 and difficult > 78:
            i, j = random.randrange(0, self.n * self.n, 1), random.randrange(0, self.n * self.n,
                                                                             1)  # Выбираем случайную ячейку
            if flook[i][j] == 0:  # Если её не смотрели
                iterator += 1
                flook[i][j] = 1  # Посмотрим

                temp = self.table[i][j]  # Сохраним элемент на случай если без него нет решения или их слишком много
                self.table[i][j] = 0
                difficult -= 1  # Усложняем если убрали элемент

                table_solution = []
                for copy_i in range(0, self.n * self.n):
                    table_solution.append(self.table[copy_i][:])  # Скопируем в отдельный список

                i_solution = 0
                for solution in solver.solve_sudoku((self.n, self.n), table_solution):
                    i_solution += 1  # Считаем количество решений

                if i_solution != 1:  # Если решение не одинственное вернуть всё обратно
                    self.table[i][j] = temp
                    difficult += 1  # Облегчаем
        self.show()
        print("difficult = ", difficult)

    @staticmethod
    def get_range(item):
        if 0 <= item < 3:
            return range(0, 3)
        elif 3 <= item < 6:
            return range(3, 6)
        else:
            return range(6, 9)

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
