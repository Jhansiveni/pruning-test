# code for alpha beta pruning test


# Simple Alpha-Beta Pruning Code

def alphabeta(depth, node, isMax, values, alpha, beta):

    # Leaf node
    if depth == 3:
        return values[node]

    # MAX player
    if isMax:
        best = -1000

        for i in range(2):
            val = alphabeta(depth + 1, node * 2 + i,
                            False, values, alpha, beta)

            best = max(best, val)
            alpha = max(alpha, best)

            # Pruning
            if beta <= alpha:
                break

        return best

    # MIN player
    else:
        best = 1000

        for i in range(2):
            val = alphabeta(depth + 1, node * 2 + i,
                            True, values, alpha, beta)

            best = min(best, val)
            beta = min(beta, best)

            # Pruning
            if beta <= alpha:
                break

        return best


