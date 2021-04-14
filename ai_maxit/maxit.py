import random

class state_maxit():
    infinity = 100

    players = ['1', '2']
    
    opponent = {'1': '2', '2': '1'}

    def __init__(self, player='1',value=None):
        if value:
            self.value = value
        else:
            self.generate_field()
            self.player = player
            #Если ни один игрок ещё не ходил, и нет ограничений на строки и столбцы
            #то присвоим координаты -1 -1, это будет означать
            #что ограничений на первый ход нет
            self.coords = [-1, -1]
            self.lastNum = 0

    def generate_field(self):
        self.value = [[], [], []]
        for row in range(3):
            for _ in range(3):
                self.value[row].append(random.randint(1, 9))
        return

    def show(self):
        for line in self.value:
            print(line)

    #Вынесем для более удобной проверки в is_win без бесконечной рекурсии
    def append(self, player, moves):
        if self.player == '1':
            if self.coords == [-1, -1]:
                for x in range(3):
                    for y in range(3):
                        moves.append((x, y, self.player))
            else:
                x, _ = self.coords
                for i in range(3):
                    if self.value[x][i] != 0:
                        moves.append((x, i, self.player))
        if self.player == '2':
            _, y = self.coords
            for i in range(3):
                if self.value[i][y] != 0:
                        moves.append((i, y, self.player))

    '''Первый игрок выбирает из строки, второй из столбца'''
    #move - (x, y, player)
    def get_moves(self, player):
        if self.is_win(player) or self.is_win(self.opponent[player]):
            return []
        moves = []
        self.append(player, moves)
        return moves

    # Ход будет списком кортежей из старых и новых координат
    def do_move(self, move):
        x, y, player = move
        self.lastNum = self.value[x][y]
        self.value[x][y] = 0
        self.coords = [x, y]
        self.player = self.opponent[player]
         
    def undo_move(self, move):
        x, y, player = move
        self.value[x][y] = self.lastNum
        self.player = self.opponent[player]

    #метод будет работать не на прямую, is_win будет показывать победу оппонента
    #название не меняем для работы остальных ранее написанных методов с применением is_win
    def is_win(self, player):
        moves = []
        self.append(player, moves)
        if moves == []:
            return True
        return False

    #будем брать максимальую цифру каждый раз (не всегда выигрышная стратегия для первого)
    def score(self, player):
        oppenent = state_maxit.opponent[player]
        if self.is_win(player):
            return (-1) * state_maxit.infinity
        elif self.is_win(oppenent):
            return state_maxit.infinity
        else:
            max = 0
            for move in self.get_moves(player):
                x, y, _ = move
                if self.value[x][y] > max:
                    max = self.value[x][y]
            return max
