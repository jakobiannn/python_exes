from base import state
from copy import deepcopy

class state_giveaway(state):
	#'''Значение бесконечности для оценочной функции'''
	infinity = 100
	players = {'W': ['W', 'WQ'], 'B': ['B', 'BQ']}
	#'''противники'''
	opponent = {'W':('B', 'BQ'), 'B':('W', 'WQ')}
	def __init__(self, field):
		#'''Конструктор класса, инициализация полей'''
		self.value = field
		print('Game is started!')

	def do_move(self, field, move):
		result = deepcopy(field)
		for(row, col), _, new_state in move:
			if(row == 0 and new_state == "W"):
				result[row][col] = "WQ"
			elif(row == 7 and new_state == "B"):
				result[row][col] = "BQ"
			else:
				result[row][col] = new_state
		return result


	def undo_move(self, move):
		for (row, col), cancel_state, _ in move:
				self.value[row][col] = cancel_state
		return self.value

	def is_win(self, player):
		#'''Проверка, что игрок player выиграл'''
		opp = self.opponent[player]
		enemyFigures = 0
		for lines in self.value:
			for row in lines:
				if(row in opp):
					enemyFigures += 1
		if enemyFigures == 0:
			return True
		return False

	#вспомогательная функция для get_moves,
	#проверим есть ли обязательные ходы и если их нет,
	#то занесем все обычные
	def append_move(self, field, moves, player, coord, a, b):
		lines, row = coord
		#проверим, существуют ли ячейки поля по диагонали
		#ячейка должна как существовать, так и не являться съеденной
		if(0 <= lines + 2*a <= 7 and 0 <= row + 2*b <= 7):
			if(field[lines + a][row + b] in self.opponent[player]):
				if((lines + a, row + b) not in moves):
					#проверим, можно ли съесть шашку(существует ли дальше поле)
						if(field[lines + 2*a][row + 2*b] == 0):
							move = []
							move.append(((lines, row), player, '0'))
							move.append(((lines+a, row+b), (lines+a, row+b), '0'))
							move.append(((lines+a*2, row+b*2), '0', player))
							moves.append(move)

	def mustHaveMoves(self, field, coord, player):
		moves = []
		self.append_move(field, moves, player, coord, -1, -1)
		self.append_move(field, moves, player, coord,  1, -1)
		self.append_move(field, moves, player, coord, -1,  1)
		self.append_move(field, moves, player, coord,  1,  1)
		return moves

	def append_common_move(self, moves, coord, player, a, b):
		lines, row = coord
		if(0 <= lines + a <= 7 and 0 <= row + b <= 7):
			if (self.value[lines + a][row + b] != player):
				move = []
				move.append(((lines, row), player,'0'))
				move.append(((lines+a, row+b), '0', player))
				moves.append(move)

	def commonMoves(self, coord, player):
		moves = []
			#условие, что шашка не стоит в верхней строчке и левом/правом столбце
			#аналогично для черных в нижней строчке и нижнем левом/правом
		if(player == 'W' or player == 'WQ' or player == 'BQ'):
			self.append_common_move(moves, coord, player, -1, 1)
			self.append_common_move(moves, coord, player, -1, -1)
				#или левом столбце
		if(player == 'B' or player == 'WQ' or player == 'BQ'):
			self.append_common_move(moves, coord, player, 1, -1)
			self.append_common_move(moves, coord, player, 1, 1)
		return moves

	def get_moves(self, player):
		# если ситуация выигрышная или проигрышная
		# то ходов нет
		if (self.is_win(player) or self.is_win(self.opponent[player][0])):
			return []
		#получим список обязательных ходов для каждой шашки
		#если есть обязательные ходы, то вернем их
		moves = []
		for lines in range(8):
			for row in range(8):
				if (self.value[lines][row] in self.players[player]):
					current_move = []
					current_move.extend(self.mustHaveMoves(self.value, (lines, row), player))
					while current_move:
						move = current_move.pop()
						new_cell = move[-1][0]
						copy_field = self.do_move(self.value, move)
						new_moves = self.mustHaveMoves(copy_field, new_cell, player)

						if new_moves:
							for new_move in new_moves:
								new_move1 = deepcopy(move)
								new_move1.extend(new_move)
								current_move.append(new_move1)
						else:
							moves.append(move)
		#если обязательных нет
		#получим список обычных ходов
		if(moves != []):
			return moves
		else:
			for lines in range(8):
				for row in range(8):
					if (self.value[lines][row] in self.players[player]):
						if(self.commonMoves((lines, row), self.value[lines][row]) != []):
							moves.extend(self.commonMoves((lines, row), self.value[lines][row]))
		return moves

	def score(self, player):
		'''Расчет оценочной функции'''
		raise NotImplementedError
