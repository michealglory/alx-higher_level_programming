#!/usr/bin/python3
"""Python Module that Solves the N-queens puzzle"""
import sys


def init_board(n):
    """
    Initialize an empty chessboard of size n x n.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list: A list representing the initialized chessboard.
    """
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return board

def board_deepcopy(board):
    """
    Create a deep copy of a given chessboard.

    Args:
        board (list): The chessboard to be copied.

    Returns:
        list: A deep copy of the input chessboard.
    """
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return board

def get_solution(board):
    """
    Get the positions of queens (marked as 'Q') on the chessboard.

    Args:
        board (list): The chessboard to search for queens.

    Returns:
        list: A list of coordinates (row, col) where queens are placed.
    """
    solution = []
    for row in range(len(board)):
        for c in range(len(board)):
            if board[row][c] == "Q":
                solution.append([row, c])
                break
    return solution

def xout(board, row, col):
    """
    Mark the spots attacked by a queen with 'x' on the chessboard.

    Args:
        board (list): The chessboard to mark.
        row (int): The row of the queen.
        col (int): The column of the queen.

    Returns:
        None
    """
    # X out all forward spots
    for spot in range(col + 1, len(board)):
        board[row][spot] = "x"
    for spot in range(col - 1, -1, -1):
        board[row][spot] = "x"
    for i_row in range(row + 1, len(board)):
        board[i_row][col] = "x"
    for i_row in range(row - 1, -1, -1):
        board[i_row][col] = "x"
    spot = col + 1
    for i_row in range(row + 1, len(board)):
        if spot >= len(board):
            break
        board[i_row][spot] = "x"
        spot += 1
    spot = col - 1
    for i_row in range(row - 1, -1, -1):
        if spot < 0:
            break
        board[i_row][spot]
        spot -= 1
    spot = col + 1
    for i_row in range(row - 1, -1, -1):
        if spot >= len(board):
            break
        board[i_row][spot] = "x"
        spot += 1
    spot = col - 1
    for i_row in range(row + 1, len(board)):
        if spot < 0:
            break
        board[i_row][spot] = "x"
        spot -= 1

def recursive_solve(board, row, queens, solutions):
    """
    Recursively find solutions to the N-Queens puzzle.

    Args:
        board (list): The chessboard.
        row (int): The current row being considered.
        queens (int): The number of queens placed on the board.
        solutions (list): A list to store the found solutions.

    Returns:
        list: A list of lists containing solutions (positions of queens).
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for i in range(len(board)):
        if board[row][i] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][i] = "Q"
            xout(tmp_board, row, i)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
