from alpha_beta import bestmove

def calc_nodes(state, level, player, opponent):
	''' Расчет количества сгенерированных узлов
		- state - начальное состояние
		- level - максимальная глубина рекрсии (количество полуходов)
		- player - игрок
		- opponent - оппонент
	'''
	_, _, nodes = bestmove(state, level, player, opponent)
	return nodes

def test_count():
	from chomp import state_chomp
	import numpy as np
	import matplotlib.pyplot as plt

	s = state_chomp('1st')
	player, opponent = '1st', state_chomp.opponent['1st']

# <<<<<<< HEAD
	lag = 1
	x = np.arange(1, 10, lag)
	y = np.array([calc_nodes(s, level, player, opponent) for level in x])
	_ = plt.figure()
	plt.plot(x, y)
	plt.title('Count of nodes')
	plt.ylabel('nodes')
	plt.xlabel('alpha-beta')
	plt.grid(True)
	plt.show()

def test_play():
	from chomp import state_chomp

	s = state_chomp('1st')
	level = 1
	player, opponent = '1st', state_chomp.opponent['1st']

	step = 1
	while not (s.is_win(player) or s.is_win(opponent)):
		move, _, _ = bestmove(s, level, player, opponent)
		print(f'Step {step}: {move}')

		s.do_move(move)
		s.show()
		if s.is_win(player):
			print(f'Player {player} win!')
			break

		step += 1
		player, opponent = opponent, player
	print('the end')

def test_time(level):
	''' Тестирование времени расчета
		level - количество полуходов, максимальная
				глубина дерева
	'''
	from chomp import state_chomp
	from timeit import Timer

	s = state_chomp('1st')
	player, opponent = '1st', state_chomp.opponent['1st']

	# lambda-функция расчета количества узлов
	f = lambda: calc_nodes(s, level, player, opponent)

	# расчет времени выполнения
	t = Timer(f)
	print("Time = ", t.timeit(number=1))

if __name__ == "__main__":
	test_count()
	test_time(4)
	test_play()
