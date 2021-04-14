from base import state


class state_match(state):
	infinity = 100
	players = ["1", "2"]
	opponent = {"1": "2", "2": "1"}

	def __init__(self, player, x=1, y=1):
		# print("Game is started!")
		self.count = 13
		self.player = player

	def do_move(self, move):
		# для более простой отмены хода запишем в кортеж смещения по x и y и прибавим их к
		# текущим значениям переменных
		self.count -= move
		self.player = state_match.opponent[self.player]

	def undo_move(self, move):
		x = move
		self.count += move
		self.player = state_match.opponent[self.player]

	def is_win(self, player):
		if self.count == 1 and self.player == player:
			return True
		return False

	def get_moves(self, player):
		# если ситуация выигрышная или проигрышная
		# то ходов нет
		if self.is_win(player) or self.is_win(self.opponent[player]):
			return []

		moves = []

		for match in range(1, 4):
			if self.count - match > 0:
				moves.append(match)
		return moves
	#оцениваться будет вхождение в границы, необходимые для победы
	#полученные эмпирическим путем
	def score(self, player):
		opponent = state_match.opponent[player]
		# если выиграл игрок, то +бесконечность
		if self.is_win(player):
			return state_match.infinity
		# если игрок проиграл, то -бесконечность
		elif self.is_win(opponent):
			return (-1) * state_match.infinity
		else:
			if 5 < self.count < 8:
				return self.count - 5
			if 8 < self.count < 11:
				return self.count - 8
			if self.count > 11:
				return self.count - 11
			else:
				return 0
