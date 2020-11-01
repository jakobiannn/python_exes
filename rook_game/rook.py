from base import state


class state_rook(state):
	infinity = 100
	players = ["1", "2"]
	opponent = {"1": "2", "2": "1"}

	def __init__(self):
		print("Game is started!")
		self.x = 1
		self.y = 1

	def do_move(self, move):
		# для более простой отмены хода запишем в кортеж смещения по x и y и прибавим их к
		# текущим значениям переменных
		x, y = move
		self.x += x
		self.y += y

	def undo_move(self, move):
		x, y = move
		self.x -= x
		self.y -= y

	def is_win(self, player):
		# для проверки достаточно, чтобы одна координата из осей была равна 8
		if (self.x == self.y == 8):
			return True
		return False

	def get_moves(self, player):
		# если ситуация выигрышная или проигрышная
		# то ходов нет
		if self.is_win(player) or self.is_win(self.opponent[player]):
			return []

		moves = []
		# всего имеем 8 - x и 8 - y ходов по каждой оси
		for x in range(8-self.x):
			moves.append((x + 1, 0))
		for y in range(8-self.y):
			moves.append((0, y + 1))
		return moves
	#Будем оценивать отклонение фигуры от диагональной позиции
	#т.к. нахождение на позиции (x,x) является выигрышной
	def score(self, player):
		oppenent = state_rook.opponent[player]
		# если выиграл игрок, то +бесконечность
		if self.is_win(player):
			return state_rook.infinity
		# если игрок проиграл, то -бесконечность
		elif self.is_win(oppenent):
			return (-1) * state_rook.infinity
		else:
			return -abs(self.x - self.y)
