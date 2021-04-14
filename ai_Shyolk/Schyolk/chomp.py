from copy import deepcopy
# 1 is chocolate part
# 2 is poisoned chocolate
# 0 is eated chocolate part
# chocolate = [
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 1, 1, 1],
# 	[2, 1, 1, 1, 1]
# ]
chocolate1 = [
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[2, 0, 0, 0, 0]
]
# chocolate2 = [
# 	[1, 0, 0, 0, 0],
# 	[1, 0, 0, 0, 0],
# 	[2, 0, 0, 0, 0]
# ]


class state_chomp:
	players = ['1st', '2nd']
	opponent = {'1st':'2nd', '2nd':'1st'}
	infinity = 100
	
	def __init__(self, player, value = None):
		if value is not None:
			self.value = value
		else:
			self.value = [
				[1, 1, 1, 1, 1],
				[1, 1, 1, 1, 1],
				[2, 1, 1, 1, 1]
			]
			self.last_field = self.value
		self.player = player

	# move is (x, y)
	def get_moves(self, player):
		if self.is_win(player) or self.is_win(self.opponent[player]):
			return []
		moves = []

		for i in range(3):
			for j in range(5):
				if self.value[i][j] == 1:
					moves.append((i, j, player))
		return moves

	def do_move(self, move):
		x, y, player = move
		self.last_field = deepcopy(self.value)
		for i in range(0, x + 1):
			for j in range(y, 5):
				self.value[i][j] = 0
		self.player = self.opponent[player]
		

	def undo_move(self, move):
		_, _, player = move
		self.value = self.last_field
		self.player = self.opponent[player]

	def is_win(self, player):
		if self.value == chocolate1:
			return True
		return False

	def show(self):
		for line in self.value:
			print(line)
		print("---------------")

	def score(self, player):
		opponent = self.opponent[player]
		if self.is_win(player):
			return self.infinity
		elif self.is_win(opponent):
			return (-1) * self.infinity
		count = 0
		for line in self.value:
			for cell in line:
				if cell == 0:
					count += 1
		return count

c = state_chomp('1st')
c.do_move((0,1,'1st'))
c.show()

# c.do_move((1,1))
# c.undo_move((1,1))
# c.do_move((1,1))
# print(c.get_moves('1st'))
# c.show()
