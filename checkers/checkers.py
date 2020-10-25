from base import state

class state_giveaway(state):
	#'''Значение бесконечности для оценочной функции'''
	infinity = 100


    #lastmove = (x1, y1, x2, y2, player)
	#'''список игроков - крестик и нолик'''
	players = ["W", "B"]
	#checkers = {'W': ['W', 'WQ'], 'B': ['B', 'BQ'],}

	#'''противники'''
	opponent = {"W":"B", "B":"W"}
	def __init__(self, value=None):
		#'''Конструктор класса, инициализация полей'''
		# если value==None, то генерируем
		# пустое поле
		if value:
			self.value = value
		else:
            # иначе создаем готовое поле
			self.value = field
		print('Game is started!')

	def do_move(self, move, eaten_figures = None):
	# ход представляет собой кортеж
	# (x1, y1, x2, y2, player)
	# где
	# - x1, y1 - начальные координаты шашки
	# - x2, y2 - конечные координаты
	# - player - игрок, который делает ход
	# координаты отсчитываются от 0 до 7
	# eaten_figures - список из списков с координатами съеденных фигур
		x1, y1, x2, y2, player = move
		self.value[x1][y1] = 0
		self.value[x2][y2] = player
		if eaten_figures != None:
			for figure in eaten_figures:
				x, y = figure
				self.value[x][y] = 0


	def undo_move(self, move, eaten_figures):
		# ход представляет собой кортеж
		# (row, col, player)
		# где
		# - row, col - координаты клетки,
		#              в которую ставится символ
		# - player - игрок, который делает ход
		x1, y1, x2, y2, player = move
		# при отмене хода мы ставим в ячейку
		# пустое значение
		self.value[x1][y1] = player
		self.value[x2][y2] = 0
		if eaten_figures != None:
			for figure in eaten_figures:
				x, y = figure
				self.value[x][y] = opponent[player]

	def is_win(self, player):
		#'''Проверка, что игрок player выиграл'''
		enemyFigures = 0
		for lines in self.value:
			for row in lines:
				if row == self.opponent[player]:
					enemyFigures += 1
		if enemyFigures == 0:
			return True
		return False
	#def kingMoves() - для оценки возможных ходов дамки

	#вспомогательная функция для get_moves,
	#проверим есть ли обязательные ходы и если их нет,
	#то занесем все обычные

	def checkSlot(self, lines, row, moves, player, eaten_figures, a, b, last, first):
		#проверим, существуют ли ячейки поля по диагонали
		#ячейка должна как существовать, так и не являться съеденной
		if(0 <= lines + a <= 7 and 0 <= row + b <= 7):
			if(self.value[lines + a][row + b] == self.opponent[player]):
				if([lines + a, row + b] not in eaten_figures):
					#проверим, можно ли съесть шашку(существует ли дальше поле)
					#с последующей проверкой с помощью рекурсии
					if(0 <= lines + 2*a <= 7 and 0 <= row + 2*b <= 7):
						if(self.value[lines + 2*a][row + 2*b] == 0):
							if(first == []):
								first += [[lines, row]]
							last = [[lines + 2*a, row + 2*b]]
							eaten_figures += [[lines + a, row + b]]
							#self.mustHaveMoves(lines + 2*a, row + 2*b, player, moves, eaten_figures, last, first)
		# moves += first
		# moves += last
		# moves += player
		return first, last, eaten_figures
	'''ИСПОЛЬЗОВАТЬ ПОЛЯ КЛАССА ДЛЯ УПРОЩЕНИЯ МЕТОДОВ'''
	def mustHaveMoves(self, lines, row, player, moves = [], eaten_figures = [], last = [], first = []):
		currentMove = []
		eatedFigure = []

		finalFirst, finalLast, eatedFigure = self.checkSlot(lines, row, moves, player, eaten_figures, 1, 1, last, first)
		moves += finalFirst
		moves += finalLast
		eaten_figures += eatedFigure

		finalFirst, finalLast, eatedFigure = self.checkSlot(lines, row, moves, player, eaten_figures, 1, -1, last, first)
		moves += finalFirst
		moves += finalLast
		eaten_figures += eatedFigure

		finalFirst, finalLast, eatedFigure = self.checkSlot(lines, row, moves, player, eaten_figures, -1, 1, last, first)
		moves += finalFirst
		moves += finalLast
		eaten_figures += eatedFigure

		finalFirst, finalLast, eatedFigure = self.checkSlot(lines, row, moves, player, eaten_figures, -1, -1, last, first)
		moves += finalFirst
		moves += finalLast
		eaten_figures += eatedFigure
		return moves, eaten_figures


	def commonMoves(self, lines, row, player):
		moves = []
		#условие, что шашка не стоит в верхней строчке и левом/правом столбце
		#аналогично для черных в нижней строчке и нижнем левом/правом
		if(player == 'W'):
			if(lines - 1 >= 0 and row + 1 <= 7):
				if (self.value[lines - 1][row + 1] != player):
						moves += [[lines, row, lines - 1, row + 1, player]]
			#или левом столбце
			if(lines - 1 <= 7 and row - 1 >= 0):
				if (self.value[lines - 1][row - 1] != player):
						moves += [[lines, row, lines - 1, row - 1, player]]
		elif(player == 'B'):
			if(lines + 1 >= 0 and row + 1 <= 7):
				if (self.value[lines - 1][row + 1] != player):
						moves += [[lines, row, lines + 1, row + 1, player]]
			#или левом столбце
			if(lines + 1 <= 7 and row - 1 >= 0):
				if (self.value[lines - 1][row - 1] != player):
						moves += [[lines, row, lines + 1, row - 1, player]]
		return moves

	def get_moves(self, player):
		# если ситуация выигрышная или проигрышная
		# то ходов нет
		if self.is_win(player) or self.is_win(self.opponent[player]):
			return []
		#получим список обязательных ходов для каждой шашки
		#если есть обязательные ходы, то вернем их
		moves = []
		eaten_figures = []
		for lines in range(8):
			for row in range(8):
				if (self.value[lines][row] == player):
					if(self.mustHaveMoves(lines, row, player) != []):
						currentMove, eatedFigure =  self.mustHaveMoves(lines, row, player)
						moves.append(currentMove)
						eaten_figures.append(eatedFigure)
		#если обязательных нет
		#получим список обычных ходов
		if(moves != []):
			return moves, eaten_figures
		else:
			for lines in range(8):
				for row in range(8):
					if self.value[lines][row] == player:
						moves += self.commonMoves(lines, row, player)
		return moves




	def score(self, player):
		#'''Расчет оценочной функции'''
		raise NotImplementedError
