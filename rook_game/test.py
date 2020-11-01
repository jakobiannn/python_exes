from rook import state_rook

game = state_rook()
game.do_move((2,5))
print(game.x, game.y)
print(game.score('2'))
