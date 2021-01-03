"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    # Creates 2 variables which will be used to track the number of turns by each
    x_turns = 0
    o_turns = 0

    # For Loop to access every row in the game board
    for row in board:

        # For Loop to access every cell in current row
        for cell in row:

            # Checks if value in current cell is "X"
            if cell == X:
                x_turns += 1

            # Checks if value in current cell is "O"
            if cell == O:
                o_turns += 1

    # Checks if the value in "x_turns" is less than or equal to "o_turns"
    if x_turns <= o_turns:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # Creates a set called "possible_moves"
    possible_moves = set()

    # For Loop to access every row in the game board
    for i, row in enumerate(board):

        # For Loop to access every cell in current row
        for j, cell in enumerate(row):

            # Check if current cell is empty
            if cell == EMPTY:
                possible_moves.add((i,j))

    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise Exception("invalid")

    b2 = copy.deepcopy(board)
    b2[action[0]][action[1]] = player(board)

    return b2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Checks to make sure first row is not blank
    if board[0][0] == board[0][1] == board[0][2] != None:

        # If "X" in Top Left Corner, Player X won
        if board[0][0] == X:
            return X

        # Else, Player O won
        else:
            return O

    # Checks to make sure second row is not blank
    elif board[1][0] == board[1][1] == board[1][2] != None:

        # If "X" in Left most column of Middle Row, Player X won
        if board[1][0] == X:
            return X

        # Else, Player O won
        else:
            return O

    # Checks to make sure third row is not blank
    elif board[2][0] == board[2][1] == board[2][2] != None:

        # If "X" in Bottom Left Corner, Player X won
        if board[2][0] == X:
            return X

        # Else, Player O won
        else:
            return O

    # Checks to make sure first column is not blank
    elif board[0][0] == board[1][0] == board[2][0] != None:

        # If "X" in Top Left Corner, Player X won
        if board[0][0] == X:
            return X

        # Else, Player O won
        else:
            return O

    # Checks to make sure second column is not blank
    elif board[0][1] == board[1][1] == board[2][1] != None:

        # If "X" in Middle column, Player X won
        if board[0][1] == X:
            return X

        # Else, Player O won
        else:
            return O

    # Checks to make sure third column is not blank
    elif board[0][2] == board[1][2] == board[2][2] != None:

        # If "X" in Top Right Corner, Player X won
        if board[0][2] == X:
            return X

        # Else, Player O won
        else:
            return O

    # Checks to make sure Diagonal is not blank
    elif board[0][0] == board[1][1] == board[2][2] != None:

        # If "X" in Top Left Corner, Player X won
        if board[0][0] == X:
            return X

        # Else, Player O won
        else:
            return O

    # Checks to make sure Diagonal is not blank
    elif board[0][2] == board[1][1] == board[2][0] != None:

        # If "X" in Top Right Corner, Player X won
        if board[0][2] == X:
            return X

        # Else, Player O won
        else:
            return O

    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Return True (meaning the game has ended) if there is a winner or there are no more actions (no empty cells left on the board)
    if winner(board) is not None or not actions(board):
        return True

    # Game has not ended, so return False
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # Stores the value returned from "winner(board)" function in the variable, "game_winner"
    game_winner = winner(board)

    # If the value in "game_winner" is "X", return 1
    if game_winner == X:
        return 1

    # If the value in "game_winner" is "O", return -1
    elif game_winner == O:
        return -1

    # Else return 0
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    # Optimization by hard coding the first move
    if board == initial_state():
        return 0, 1

    current = player(board)
    best_value = float("-inf") if current == X else float("inf")

    for action in actions(board):
        new_value = minimax_value(result(board, action), best_value)

        if current == X:
            new_value = max(best_value, new_value)

        if current == O:
            new_value = min(best_value, new_value)

        if new_value != best_value:
            best_value = new_value
            best_action = action

    return best_action


def minimax_value(board, best_value):
    """
    Returns the best value for each recursive minimax iteration.
    """
    if terminal(board):
        return utility(board)

    turn = player(board)
    value = float("-inf") if turn == X else float("inf")

    for action in actions(board):
        new_value = minimax_value(result(board, action), value)

        if turn == X:
            if new_value > best_value:
                return new_value
            value = max(value, new_value)

        if turn == O:
            if new_value < best_value:
                return new_value
            value = min(value, new_value)

    return value