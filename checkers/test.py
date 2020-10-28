from checkers import state_giveaway
# # from minimax import bestmove
# from negmax import bestmove

# if __name__ == "__main__":
#     s = state_xo()
#     level = 6
#     player, opponent = "X", state_xo.opponent["X"]

#     move = bestmove(s, level, player, opponent)

#     print(f"Best move is: ", move)
global field
field = [[0,"B",0,"B",0,"B",0,"B"],
        ["B",0,"B",0,"B", 0,"B",0],
        [0,"B",0,"B",0,"B",0,"B"],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        ["W",0,"W",0,"W",0,"W",0],
        [0,"W",0,"W",0,"W",0,"W"],
        ["W",0,"W",0,"W",0,"W",0]]
game = state_giveaway(field)
print(game.get_moves("W"))
