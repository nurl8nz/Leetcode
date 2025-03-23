from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row, cols, diagonals, anti_diagonals, board):
            if row == n:
                solutions.append(["".join(row) for row in board])
                return

            for col in range(n):
                diag, anti_diag = row - col, row + col
                if col in cols or diag in diagonals or anti_diag in anti_diagonals:
                    continue

                cols.add(col)
                diagonals.add(diag)
                anti_diagonals.add(anti_diag)
                board[row][col] = 'Q'

                backtrack(row + 1, cols, diagonals, anti_diagonals, board)

                cols.remove(col)
                diagonals.remove(diag)
                anti_diagonals.remove(anti_diag)
                board[row][col] = '.'

        solutions = []
        board = [['.'] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), board)
        return solutions
