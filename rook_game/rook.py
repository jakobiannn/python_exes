from base import state


class state_rook(state):
    infinity = 100
    players = ["1", "2"]
    opponent = {"1": "2", "2": "1"}

    def __init__(self, value=None):
        if value:
            self.value = value
        else:
            self.value = [0, 0]

    def __str__(self):
        s = ""
        for row in self.value:
                if row == None:
                    s += "[ ]"
        else:
            s += f"[{row}]"
        s += '\n'
        return s

    def do_move(self, move):
        # для более простой отмены хода запишем в кортеж смещения по x и y и прибавим их к
        # текущим значениям переменных
        x, y, player = move
        self.x += x
        self.y += y
        self.value[self.x, self.y] = player

    def undo_move(self, move):
		x, y, _ = move
        self.x -= x
        self.y -= x
		self.value[self.x, self.y] = player

    def is_win(self, player):
        # для проверки достаточно, чтобы одна координата из осей была равна 8
        if self.x == 8 or self.y == 8:
            return True
        return False

    def get_moves(self, player):
        # если ситуация выигрышная или проигрышная
        # то ходов нет
        if self.is_win(player) or self.is_win(self.opponent[player]):
            return []

        moves = []
        # всего имеем 8 - x и 8 - y ходов по каждой оси
        for x in range(8 - self.x):
            for y in range(8 - self.y):
                moves.append((self.x + x + 1, self.y + y + 1, player))
        return moves

    def score(self, player):
        oppenent = state_rook.opponent[player]
        # если выиграл игрок, то +бесконечность
        if self.is_win(player):
            return state_rook.infinity
        # если игрок проиграл, то -бесконечность
        elif self.is_win(oppenent):
            return (-1) * state_rook.infinity
        else:
            # в противном случае выведем количество возможных ходов
            return len(self.get_moves(player))
