"""
Tic Tac Toe Player
"""
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
    lines = list(board)
    wpossibilities = lines
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
    if winner(board) == None or actions(board) == False:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
