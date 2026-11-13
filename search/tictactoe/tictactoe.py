import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    cells = [cell for rows in board for cell in rows]
    x_count = cells.count(X)
    o_count = cells.count(O)
    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    cells = [(i,j) for i, row in enumerate(board) for j, cell in enumerate(row) if cell == EMPTY]
    return set(cells)


def result(board, action):
    new_board = copy.deepcopy(board)
    i, j = action
    if action not in actions(board):
        raise Exception("invalid action")
    if player(board) == X:
        new_board[i][j] = X
    else:
        new_board[i][j] = O
    return new_board

def winner(board):
    wpossibilities = list(board)
    for j in range(3):
        column = [board[i][j] for i in range(3)]
        wpossibilities.append(column)
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[0][2], board[1][1], board[2][0]]
    wpossibilities.append(diagonal1)
    wpossibilities.append(diagonal2)
    for line in wpossibilities:
        a, b, c = line
        if a == b == c and a != EMPTY:
            return a
    return None
        
def terminal(board):
    return winner(board) is not None or not actions(board)


def utility(board):
    w = winner(board) 
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0

def max_value(board):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    if terminal(board):
        return None
    turn = player(board)

    if turn == X:
        best_score = -math.inf
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            v = min_value(new_board)
            if v > best_score:
                best_score = v
                best_action = action
        return best_action
        
    if turn == O:
        best_score = math.inf
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            v = max_value(new_board)
            if v < best_score:
                best_score = v
                best_action = action
        return best_action
