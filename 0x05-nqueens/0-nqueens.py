#!/usr/bin/python3
"""
This module defines functions used to solve the N queens  puzzle, the
challenge of placing N non-attacking queens on an NxN chessboard.
"""
import sys


def safe(bod, row, colm, N):
    """
    Function checks whether a queen can be placed on board[row][colm]
    DOne by checking the colm, upper and lower diagonals
    """
    for i in range(row):  # left side column
        if bod[i] == colm:
            return False

    for i, j in zip(range(row-1, -1, -1), range(colm-1, -1, -1)):
        if bod[i] == j:  # left side upper diagonal
            return False

    for i, j in zip(range(row-1, -1, -1), range(colm+1, N)):
        if bod[i] == j:  # left side lower diagonal
            return False
    return True

def solve_nqueens(N, row, bod, solns):
    """
    Use backtracking to solve N queens, placing the queens recursively and
    ensuring that no two queens are attacking each other
    """
    if row == N:
        solns.append([[i, bod[i]] for i in range(N)])
        return

    for colm in range(N):
        if safe(bod, row, colm, N):
            bod[row] = colm
            solve_nqueens(N, row + 1, bod, solns)

def nqueens(N):
    bod = [-1] * N
    solns = []
    solve_nqueens(N, 0, bod, solns)
    for soln in solns:
        print(soln)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)
