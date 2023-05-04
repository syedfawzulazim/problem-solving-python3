from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        numsOfIslands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            q = deque()
            q.append((row,col))
            while q:
                r, c = q.popleft()
                visited.add((r,c))
                for ro, co in directions:
                    r1 = r + ro
                    c1 = c + co
                    if (r1 in range(rows) 
                        and c1 in range(cols) 
                        and (r1,c1) not in visited
                        and grid[r1][c1] == '1'
                        ):
                      
                        q.append((r1,c1))
                        visited.add((r1,c1))


        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    numsOfIslands += 1
                    bfs(r,c)
                
        return numsOfIslands

S = Solution()
print(S.numIslands([
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]]
    ))