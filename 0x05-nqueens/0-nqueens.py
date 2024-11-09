#!/usr/bin/python3
'''N Queens Challenge'''

import sys


def solve_nqueens(n):
    """Solve the N-Queens puzzle and return all possible solutions"""
    solutions = []
    placed_queens = []  # coordinates format [row, column]

    def is_safe(row, col):
        """Check if placing a queen at (row, col) is safe"""
        for r, c in placed_queens:
            if col == c or row - col == r - c or row + col == r + c:
                return False
        return True

    def backtrack(row):
        """Backtrack to solve the problem recursively"""
        if row == n:
            solutions.append(placed_queens[:])
            return

        for col in range(n):
            if is_safe(row, col):
                placed_queens.append([row, col])
                backtrack(row + 1)
                placed_queens.pop()  # Backtrack

    backtrack(0)
    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)

    for idx, solution in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(solution, end="")
        else:
            print(solution)
