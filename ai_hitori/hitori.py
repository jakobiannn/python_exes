from copy import deepcopy

from base import base_state
import random


class state_hitori(base_state):

    def __init__(self, parent=None, initial=None, depth=0, n=3):
        self.n = n
        self._depth = depth
        self.parent = parent
        if initial is not None:
            self.field = initial
        else:
            self.field = [[i for i in range(n)] for x in range(n)]
            for i in range(n):
                for j in range(n):
                    self.field[i][j] = random.randint(1, n)

    def __hash__(self):
        hash_num = ""
        for row in self.field:
            for col in row:
                hash_num += str(col)
        return int(hash_num)

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def show(self):
        for row in self.field:
            print(row)
        print('---------------------')

    def is_append(self, row, col):
        bubble = self.field[row][col]
        if bubble == 0:
            return False
        self.field[row][col] = 0
        for i in range(self.n):
            if self.field[i][col] == bubble or self.field[row][i] == bubble:
                self.field[row][col] = bubble
                return True
        self.field[row][col] = bubble
        return False

    def get_moves(self):
        moves = []
        for row in range(self.n):
            for col in range(self.n):
                if self.is_append(row, col):
                    new_table = deepcopy(self.field)
                    new_table[row][col] = 0
                    moves.append(state_hitori(self, new_table, self._depth + 1))
        return moves

def fair_evaluator(initial, goal):
	sum = 0
	for line in 3:
		for row in 3:
			if initial.field[line][row] == 0:
				if line == 0:
					sum += 100
				elif line == 1:
					sum += 10
				elif line == 2:
					sum += 1
	return sum
