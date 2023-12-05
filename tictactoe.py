"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def check_initial_state(board):
    """
    Returns wether state of the board of initial state.
    """
    xCount = sum(row.count(X) for row in board)
    oCount = sum(row.count(O) for row in board)
    return xCount == 0 and oCount == 0


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = sum(row.count(X) for row in board)
    oCount = sum(row.count(O) for row in board)
    
    return X if xCount <= oCount else O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i,j) for i in range(3) for j in range(3) if board[i][j] is EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not Possible Action")
    
    board_copy = copy.deepcopy(board)
    i,j = action
    board_copy[i][j] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in [X,O]:

        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
                return player
            
        if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
            return player
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return True
    if winner_player == O:
        return True
    for row in board:
        for col in row:
            if col == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    elif player(board) == X:
        return max(actions(board), key= lambda action : MinValue(result(board,action)))
    
    elif player(board) == O:
        return min(actions(board), key= lambda action : MaxValue(result(board,action)))

    
def MaxValue(board):
    """
    Returns the maximum utility value among all possible minimum values for the current state of the board.
    """
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v,MinValue(result(board,action)))
    return v

def MinValue(board):
    """
    Returns the minimum utility value among all possible maximum values for the current state of the board.
    """
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, MaxValue(result(board,action)))
    return v