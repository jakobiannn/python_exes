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

def test_play():
	from cop_thug import state_ct

	s = state_ct()
	level = 4
	player, opponent = "C", "T"

	print('start!')

	step = 1
	while not (s.is_win(player) or s.is_win(opponent)):
		move, _, _ = bestmove(s, level, player, opponent)
		if move == None:
			print('finish... draw')
			break
		print(f'Step {step}: {move}')

		s.do_move(move)

		if s.is_win(opponent):
			print(f'Player {opponent} win!')
			break

		step += 1
		player, opponent = opponent, player

	print('the end')

def test_time(level):
	''' Тестирование времени расчета
		level - количество полуходов, максимальная
				глубина дерева
	'''

	from cop_thug import state_ct
	from timeit import Timer

	s = state_ct()
	player, opponent = "C", "T"

	# lambda-функция расчета количества узлов
	f = lambda: calc_nodes(s, level, player, opponent)

	# расчет времени выполнения
	t = Timer(f)
	print("Time = ", t.timeit(number=1))

def calc_nodes(state, level, player, opponent):
	''' Расчет количества сгенерированных узлов
		- state - начальное состояние
		- level - максимальная глубина рекрсии (количество полуходов)
		- player - игрок
		- opponent - оппонент
	'''
	_, _, nodes = bestmove(state, level, player, opponent)
	return nodes

def test_plot():
	from cop_thug import state_ct
	import numpy as np
	import matplotlib.pyplot as plt
	s = state_ct()
	player, opponent = 'C', 'T'

	# правая граница для графика
	depth = 6
	x = np.arange(1, depth, 1)
	y = np.array([calc_nodes(s, level, player, opponent) for level in x])
	_ = plt.figure()
	plt.plot(x, y)
	plt.title('Count of nodes')
	plt.ylabel('nodes')
	plt.xlabel('minimax')
	plt.grid(True)
	plt.show()

if __name__ == "__main__":
	test_play()
	test_plot()
	test_time(4)
