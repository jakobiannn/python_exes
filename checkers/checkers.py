from base import state
from copy import deepcopy

class state_checkers(state):
	#'''Значение бесконечности для оценочной функции'''
	infinity = 100
	players = {'W': ['W', 'WQ'], 'B': ['B', 'BQ']}
	#'''противники'''
	opponent = {'W':('B', 'BQ'), 'B':('W', 'WQ')}
	def __init__(self, field):
		#'''Конструктор класса, инициализация полей'''
		self.value = field

	def do_move(self, field, move):
		result = deepcopy(field)
		#Если шашка дошла до конца поля, то она становится дамкой
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

	def is_win(self, player):
		#'''Проверка, что игрок player выиграл'''
		figures = 0
		for lines in self.value:
			for row in lines:
				if(row in self.opponent[player]):
					figures += 1
		if figures == 0:
			return True
		return False

	#вспомогательная функция для get_moves, добавляет ходы со взятием
	#с каждой стороны от шашки
	def append_move(self, field, moves, player, coord, a, b):
		lines, row = coord
		#проверим, существуют ли ячейки поля по диагонали
		if(0 <= lines + 2*a <= 7 and 0 <= row + 2*b <= 7):
			if(field[lines + a][row + b] in self.opponent[player]):
				if((lines + a, row + b) not in moves):
						if(field[lines + 2*a][row + 2*b] == '0'):
							move = []
							move.append(((lines, row), player, '0'))
							move.append(((lines+a, row+b), self.opponent[player][0], '0'))
							move.append(((lines+a*2, row+b*2), '0', player))
							moves.append(move)
	#добавляем ходы со взятием
	def mustHaveMoves(self, field, coord, player):
		moves = []
		self.append_move(field, moves, player, coord, -1, -1)
		self.append_move(field, moves, player, coord,  1, -1)
		self.append_move(field, moves, player, coord, -1,  1)
		self.append_move(field, moves, player, coord,  1,  1)
		return moves
	#проверка для обычных ходов без взятия
	def append_common_move(self, moves, coord, player, a, b):
		lines, row = coord
		if(0 <= lines + a <= 7 and 0 <= row + b <= 7):
			if (self.value[lines + a][row + b] != player):
				move = []
				move.append(((lines, row), player,'0'))
				move.append(((lines+a, row+b), '0', player))
				moves.append(move)
	#добавляем обычные ходы без взятия, с учетом наличия дамок
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
	''' Для оценочной функии воспользуемся следующими вспомогательными функицями
		Разницы между количеством съеденных своих и чужих шашек
		Разницы между количеством своих дамок и противника
		Расстоянии шашек от первой линии противника (только тех, что еще не дамки)
		Разницы в количестве возможных своих ходов и противника (заблокированные шашки) '''
	def count_eaten(self, player):
		enemyes = 0
		for line in self.value:
			for row in line:
				if row in self.opponent[player]:
					enemyes += 1
		return 12 - enemyes

	def queen(self, player):
		Q = 0
		for line in self.value:
			for row in line:
				if row == self.opponent[player][1]:
					Q += 1
		return Q

	def zero_line(self, player):
		for line in range(8):
			for row in range(8):
				if self.value[line][row] == "W":
					return line
				if self.value[line][row] == "B":
					return 7 - line

	def moves_value(self, player):
		return len(self.get_moves(player))

	def score(self, player):
		opponent = self.opponent[player][0]
		# если выиграл игрок, то +бесконечность
		if self.is_win(player):
			return self.infinity
		# если игрок проиграл, то -бесконечность
		elif self.is_win(opponent):
			return (-1)*self.infinity
		else:
		#сложим все очки из каждого праметра игровой ситуации
		#и вернем их суммированное значение
			eaten_dif = self.count_eaten(player) - self.count_eaten(opponent)
			queen_dif = self.queen(player) - self.queen(opponent)
			line_dif = self.zero_line(player) - self.zero_line(opponent)
			moves_dif = self.moves_value(player) - self.moves_value(opponent)
		return (-1) * eaten_dif + queen_dif + line_dif + moves_dif
