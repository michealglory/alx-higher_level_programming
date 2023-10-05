#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].

    Args:
        board (list): The current state of the chessboard.
        row (int): The row where the queen is to be placed.
        col (int): The column where the queen is to be placed.

    Returns:
        bool: True if it's safe to place the queen, False otherwise.
    """
    # Check the left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower-left diagonal
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, col):
    """
    Recursive utility function to find all solutions to the N Queens puzzle.

    Args:
        board (list): The current state of the chessboard.
        col (int): The current column to consider.

    Returns:
        list: List of solutions found.
    """
    n = len(board)
    if col == n:
        # We have placed all queens successfully in this configuration
        return [board]
    
    solutions = []
    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1
            solutions += solve_n_queens_util(board, col + 1)
            board[i][col] = 0  # Backtrack
    
    return solutions

def solve_n_queens(n):
    """
    Find all solutions to the N Queens puzzle.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Returns:
        list: List of solutions found.
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize an empty chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    solutions = solve_n_queens_util(board, 0)
    
    return solutions

def print_solutions(solutions):
    """
    Print the solutions to the N Queens puzzle.

    Args:
        solutions (list): List of solutions found.
    """
    for solution in solutions:
        for row in solution:
            print("".join("Q" if cell == 1 else "." for cell in row))
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_n_queens(n)
    print_solutions(solutions)
