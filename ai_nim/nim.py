from copy import deepcopy

from base import state
import random


class state_nim(state):
    players = '1', '2'
    infinity = 100
    opponent = {'1': '2', '2': '1'}

    def __init__(self, player, n=3):
        self.heaps = []
        self.n = n
        self.player = player
        for _ in range(self.n):
            self.heaps.append(random.randint(1, 10))
        print(self.heaps)
        print("--------------------------")

    def get_moves(self, player):
        if self.is_win(player) or self.is_win(self.opponent[player]):
            return []

        moves = []
        copy_heaps = deepcopy(self.heaps)
        for heap in range(self.n):
            while copy_heaps[heap] > 0:
                moves.append((heap, copy_heaps[heap]))
                copy_heaps[heap] -= 1
        return moves

    def do_move(self, move):
        heap, stone = move
        self.heaps[heap] -= stone
        self.player = self.opponent[self.player]

    def undo_move(self, move):
        heap, stone = move
        self.heaps[heap] += stone
        self.player = self.opponent[self.player]

    def is_win(self, player):
        for heap in range(self.n):
            if self.heaps[heap] != 0:
                return False
        return True

    # оценочная функция
    # если куч больше двух, берем целую кучу
    # как только их становится две, берем во второй так, чтобы там остался один камень
    # как только остается 1 куча, берем её целиком
    def score(self, player):
        opponent = self.opponent[player]
        # если выиграл игрок, то +бесконечность
        if self.is_win(player):
            return self.infinity
        # если игрок проиграл, то -бесконечность
        elif self.is_win(opponent):
            return (-1) * self.infinity
        else:
            count = 0
            for heap in range(self.n):
                if self.heaps[heap] != 0:
                    count += 1
            if count > 2:
                for heap in range(self.n):
                    if self.heaps[heap] != 0:
                        return self.heaps[heap]
            if count == 2:
                for heap in range(self.n):
                    if self.heaps[heap] != 0:
                        return self.heaps[heap] - 1
            if count == 1:
                for heap in range(self.n):
                    if self.heaps[heap] != 0:
                        return self.heaps[heap]


s = state_nim('1')
print(s.get_moves('1'))
