from alpha_beta import bestmove
global field
field = [[0,"B",0,"B",0,"B",0,"B"],
		["B",0,"B",0,"B",0,"B",0],
		[ 0,"B",0,"B",0,"B",0,"B"],
		[ 0, 0, 0, 0, 0, 0, 0, 0],
		[ 0, 0, 0, 0, 0, 0, 0, 0],
		["W",0,"W",0,"W",0,"W",0],
		[ 0,"W",0,"W",0,"W",0,"W"],
		["W",0,"W",0,"W",0,"W",0]]
def calc_nodes(state, level, player, opponent):
	''' Расчет количества сгенерированных узлов
		- state - начальное состояние
		- level - максимальная глубина рекрсии (количество полуходов)
		- player - игрок
		- opponent - оппонент
	'''
	global nodes
	nodes = 0
	_ = bestmove(state, level, player, opponent)
	return nodes

def test_play():
	from checkers import state_checkers

	s = state_checkers(field)
	level = 4
	player, opponent = "W", state_checkers.opponent["W"][0]

	print('start!')

	step = 1
	while not (s.is_win(player) or s.is_win(opponent)):
		move, _ = bestmove(s, level, player, opponent)
		if move == None:
			print('finish... draw')
			break
			print(f'Step {step}: {move}')

		s.value = s.do_move(s.value, move)

		if s.is_win(player):
			print(f'Player {player} win!')
			break

		step += 1
		player, opponent = opponent, player

	print('the end')

if __name__ == "__main__":
	test_play()
