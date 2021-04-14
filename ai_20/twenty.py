class state_twenty:
    players = [1, 2]
    opponent = {1: 2, 2: 1}
    infinity = 100

    def __init__(self, player = 1, value = None):
        if value is not None:
            self.value = value
        else:
            self.value = ""
        self.player = player

    def get_moves(self, player):
        if len(self.value) == 0:
            return ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        else:
            return ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    #move is number wich player added to number
    def do_move(self, move):
        self.value += move              
        self.player = self.opponent[self.player]

    def undo_move(self, move):
        self.value = self.value[:-1]               
        self.player = self.opponent[self.player]

    def is_win(self, player):
        if len(self.value) == 20:
            if int(self.value) % 7 == 0 and player == 1:
                return True
            elif int(self.value) % 7 != 0 and player == 2:
                return True
        return False

    def score(self, player):
        opponent = self.opponent[player]
        # если выиграл игрок, то +бесконечность
        if self.is_win(player):
            return self.infinity
        # если игрок проиграл, то -бесконечность            
        elif self.is_win(opponent):
            return (-1)*self.infinity 
        else:
            copy_num = self.value
            if len(self.value) != 19:
                return 1
            elif len(self.value) == 19:
                for i in range (10):
                    copy_num += str(i)
                    if int(copy_num) % 7 == 0 and self.player == 1:
                        return self.infinity
                    if int(copy_num) % 7 != 0 and self.player == 2: 
                        return self.infinity
                    elif int(copy_num) % 7 != 0 and self.player == 1:
                        return (-1) * self.infinity
                    elif int(copy_num) % 7 == 0 and self.player == 2:
                        return (-1) * self.infinity
                    copy_num = copy_num[:-1]