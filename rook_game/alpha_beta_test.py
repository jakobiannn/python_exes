from alpha_beta import bestmove

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
	from rook import state_rook

	s = state_rook()
	level = 4
	player, opponent = "1", "2"

	print('start!')

	step = 1
	while not (s.is_win(player) or s.is_win(opponent)):
		move, _ = bestmove(s, level, player, opponent)
		if move == None:
			print('finish... draw')
			break
		print(f'Step {step}: {move} (x: {s.x} y: {s.y}) Player: {player}')

		s.do_move(move)

		if s.is_win(player):
			print(f'Player {player} win!')
			break

		step += 1
		player, opponent = opponent, player

	print('the end')

if __name__ == "__main__":
	test_play()
