from math import sqrt

from base import state

# Класс для описания состояния -
# игровой ситуации при игре в "Бандита и Полицейского" 10х10.

        #0   #1   #2   #3   #4   #5   #6   #7   #8   #9
box = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],  # 0
       ['W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],  # 1
       ['W', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'W'],  # 2
       ['W', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', 'W'],  # 3
       ['W', ' ', ' ', 'T', ' ', 'x', ' ', 'x', ' ', 'W'],  # 4
       ['W', ' ', 'x', ' ', 'x', 'C', ' ', ' ', ' ', 'W'],  # 5
       ['W', ' ', ' ', ' ', ' ', 'x', 'x', ' ', 'x', 'W'],  # 6
       ['W', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', 'W'],  # 7
       ['W', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'W'],  # 8
       ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']  # 9
       ]


class state_ct(state):
    """Значение бесконечности для оценочной функции"""
    infinity = 100

    '''Игроки - полицейский C (Cop) и бандит T (Thug)'''
    players = ['C', 'T']

    '''Противники'''
    opponent = {'C': 'T', 'T': 'C'}

    def __init__(self, value=None):
        if value:
            self.value = value
        else:
            self.field = box

    '''представления состояния в виде строки'''

    def __str__(self):
        s = ""
        for row in self.value:
            for item in row:
                if item is None:
                    s += "[ ]"
                else:
                    s += "[%s]" % item
            s += '\n'
        return s

    def is_append(self, coord, player):
        row, col = coord
        if self.field[row][col] == ' ':
            return True
        if player == 'T':
            if self.field[row][col] == 'W':
                return True
        return False

    def add_moves(self, coord, player, moves):
        row, col = coord
        if self.is_append((row + 1, col), player): moves.append([(row, col), (row + 1, col), player])
        if self.is_append((row, col + 1), player): moves.append([(row, col), (row, col + 1), player])
        if self.is_append((row - 1, col), player): moves.append([(row, col), (row - 1, col), player])
        if self.is_append((row, col - 1), player): moves.append([(row, col), (row, col - 1), player])

        if player == 'C':
            if self.is_append((row + 1, col + 1), player): moves.append([(row, col), (row + 1, col + 1), player])
            if self.is_append((row + 1, col - 1), player): moves.append([(row, col), (row + 1, col - 1), player])
            if self.is_append((row - 1, col + 1), player): moves.append([(row, col), (row - 1, col + 1), player])
            if self.is_append((row - 1, col - 1), player): moves.append([(row, col), (row - 1, col - 1), player])

    def get_moves(self, player):
        # если ситуация выигрышная или проигрышная
        # то ходов нет
        if self.is_win(player) or self.is_win(self.opponent[player]):
            return []
        moves = []
        for row in range(9):
            for col in range(9):
                if self.field[row][col] == player:
                    self.add_moves((row, col), player, moves)
        return moves

    # Ход будет списком кортежей из старых и новых координат
    def do_move(self, move):
        (oldrow, oldcol), (newrow, newcol), player = move
        self.field[oldrow][oldcol] = ' '
        self.field[newrow][newcol] = player

    def undo_move(self, move):
        (oldrow, oldcol), (newrow, newcol), player = move
        self.field[oldrow][oldcol] = player
        self.field[newrow][newcol] = ' '

    def is_win_cop(self):
        for row in range(9):
            for col in range(9):
                if self.field[row][col] == self.opponent['C']:
                    return False
        return True

    def is_win_thug(self, row, col):
        if row == 0 or col == 0 or row == 9 or col == 9:
            return True
        return False

    def is_win(self, player):
        for row in range(9):
            for col in range(9):
                if self.field[row][col] == player:
                    if player == 'C':
                        return self.is_win_cop()
                    if player == 'T':
                        return self.is_win_thug(row, col)

    '''оценочная функция'''

    def score_cop(self):
        c_row, c_col, t_row, t_col = 0, 0, 0, 0
        for row in range(9):
            for col in range(9):
                if self.field[row][col] == 'C':
                    c_row, c_col = row, col
                if self.field[row][col] == 'T':
                    t_row, t_col = row, col
        return (-1)*sqrt((t_row-c_row)**2 + (t_col-c_col)**2)

    def score_thug(self):
        for row in range(9):
            for col in range(9):
                if self.field[row][col] == 'T':
                    if row < col:
                        return -row
                    else:
                        return -col

    def score(self, player):
        oppenent = state_ct.opponent[player]
        if self.is_win(player):
            return (-1) * state_ct.infinity
        elif self.is_win(oppenent):
            return state_ct.infinity
        else:
            if player == 'C':
                return self.score_cop()
            if player == 'T':
                return self.score_thug()

# s = state_ct()
# print(s.get_moves('T'))
