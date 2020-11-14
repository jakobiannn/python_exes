from alpha_beta import bestmove

field = [
    ['0', 'B', '0', 'B', '0', 'B', '0', 'B'],
    ['B', '0', 'B', '0', 'B', '0', 'B', '0'],
    ['0', 'B', '0', 'B', '0', 'B', '0', 'B'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['W', '0', 'W', '0', 'W', '0', 'W', '0'],
    ['0', 'W', '0', 'W', '0', 'W', '0', 'W'],
    ['W', '0', 'W', '0', 'W', '0', 'W', '0']]


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
    from checkers import state_checkers
    import numpy as np
    import matplotlib.pyplot as plt

    s = state_checkers(field)
    player, opponent = "W", state_checkers.opponent["W"][0]

# <<<<<<< HEAD
    lag = 1
    x = np.arange(1, 8, lag)
    y = np.array([calc_nodes(s, level, player, opponent) for level in x])
    _ = plt.figure()
    plt.plot(x, y)
    plt.title('Count of nodes')
    plt.ylabel('nodes')
    plt.xlabel('alpha-beta')
    plt.grid(True)
    plt.show()

def test_play():
    from checkers import state_checkers

    s = state_checkers(field)
    level = 4
    player, opponent = 'W', state_checkers.opponent['W'][0]

    step = 1
    while not (s.is_win(player) or s.is_win(opponent)):
        move, _, _ = bestmove(s, level, player, opponent)
        print(f'Step {step}: {move}')
        if move is None:
            print('finish... draw')
            break

        s.value = s.do_move(s.value, move)
        if s.is_win(player):
            print(f'Player {opponent} win!')
            break

        step += 1
        player, opponent = opponent, player
    # for line in s.value:
    # 	print(line)
    # print("---------------------------")
    for line in s.value:
        print(line)
    print('the end')


if __name__ == "__main__":
    test_count()
    test_play()
