#!/usr/bin/env python3
import sys

def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)

def solve_nqueens(N):
    def is_safe(queens, row, col):
        for r, c in queens:
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def place_queens(row, queens):
        if row == N:
            print(queens)
            return

        for col in range(N):
            if is_safe(queens, row, col):
                queens.append([row, col])
                place_queens(row + 1, queens)
                queens.pop()

    place_queens(0, [])

if __name__ == "__main__":
    main()
