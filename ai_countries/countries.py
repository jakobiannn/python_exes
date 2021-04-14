from copy import deepcopy

from base import base_state

boards = {
	'К': ['П', 'Р', 'Ф'],
	'П': ['К', 'Р'],
	'Р': ['К', 'Ф', 'П'],
	'Ф': ['К', 'Р']
}
countries_colours = {
	'К': None,
	'П': None,
	'Р': None,
	'Ф': None
}


class state_countries(base_state):
	used_colors = set()
	unused_colors = set(['red', 'blue', 'black', 'white'])

	def __init__(self, parent=None, data=None, depth=0):
		self.parent = parent
		self._depth = depth
		if data is not None:
			self.boards = data
		else:
			self.boards = countries_colours


	def __hash__(self):
		hash = ''
		for key in self.boards:
			hash += str(countries_colours[key])
		return hash

	def __eq__(self, other):
		return self.__hash__() == other.__hash__()

	def get_moves(self):
		moves = []
		for key in boards:
			cant_use = set()
			for country in boards[key]:
				#print(f'current country:{key} color:     {self.boards[key]}')
				if self.boards[key] is not None:
					continue
				else:
				#    print(f'boards: {self.boards[country]}')
					if self.boards[country] is not None:
						cant_use.add(self.boards[country])
						self.used_colors.add(self.boards[country])
						if self.boards[country] in self.unused_colors:
							self.unused_colors.remove(self.boards[country])

			if self.used_colors != []:
				for color in self.used_colors:
					if (color not in cant_use) and (self.boards[key] is None):
						copy_board = deepcopy(self.boards)
						copy_board[key] = color
						moves.append(state_countries(self, copy_board, self._depth + 1))
			#print(cant_use, self.used_colors)
			if cant_use == self.used_colors:
				for color in self.unused_colors:
					if self.boards[key] is None:
						copy_board = deepcopy(self.boards)
						copy_board[key] = color
						moves.append(state_countries(self, copy_board, self._depth + 1))
		# print(self.used_colors)
		# print(self.unused_colors)
		return moves

def fair_evaluator(initial, goal):
	count = 0
	for key in initial:
		if initial[key] is not None:
			count += 1
	return count
