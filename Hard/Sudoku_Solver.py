from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows, cols, boxes = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        empty_cells = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + c // 3].add(num)

        def solve(index=0):
            if index == len(empty_cells):
                return True
            
            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + c // 3
            
            for num in map(str, range(1, 10)):
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_idx]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)

                    if solve(index + 1):
                        return True
                    
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)
            
            return False
        
        solve()
