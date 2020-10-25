from rook import state_rook

nodes = 0


def alpha_beta(state, level, player, opponent, low, high):
    best_move, best_score = None, None

    moves = state.get_moves(player)

    global nodes
    nodes += len(moves)

    if level == 0 or moves == []:
        return None, state.score(player)

    for m in moves:
        state.do_move(m)
        _, score = alpha_beta(state, level - 1, opponent, player, -high, -low)

        state.undo_move(m)

        if best_score == None or -1 * score > best_score:
            low = -1 * score
            best_move, best_score = m, -1 * score

        if low >= high:
            return best_move, best_score

    return best_move, best_score


def bestmove(state, level, player, opponent):
    return alpha_beta(state, level, player, opponent,
                      -state_rook.infinity, state_rook.infinity)