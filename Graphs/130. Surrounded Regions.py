from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        notFlip = set()

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in notFlip or board[r][c] == "X":
                return
        
            notFlip.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0,c)
            if board[rows-1][c] == "O":
                dfs(rows-1,c)
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][cols-1] == "O":
                dfs(r,cols-1)
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in notFlip and board[r][c] == "O":
                    board[r][c] = "X"
        
        print(notFlip)
        print(board)

        


S = Solution()
S.solve([["X","O","X"],
 ["O","X","O"],
 ["X","O","X"]])

# [["X","O","X"],
#  ["O","X","O"],
#  ["X","O","X"]]