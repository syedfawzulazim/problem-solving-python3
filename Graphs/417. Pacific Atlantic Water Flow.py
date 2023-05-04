from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        # r = (0, c) or c = (r, 0)  == pac
        # r = len(grid) - 1 or c = len(grid[0]) -1  == atl
        # alt =( r + 1, c), (r, c + 1) // if false 
        # pac = (r - 1, c), (r, c - 1)

        pac = [(-1, 0), (0, -1)]
        alt = [(1, 0), (0, 1)]

        result = []
        def bfs(r, c):

            q = deque()
            q.append((r,c))

            
            
            while q:
                r1, c1 = q.popleft()
                
                countPac = 0
                countAlt = 0

                for r2, c2 in pac:
                    rw, cl = r1+r2, c1+c2
                    if rw in range(rows) and cl in range(cols) and grid[rw][cl] <= grid[r1][c1]:
                        q.append(rw,cl)
                    else:
                        countPac += 1
                

                for r2, c2 in alt:
                    rw, cl = r1+r2, c1+c2
                    if rw in range(rows) and cl in range(cols) and grid[rw][cl] <= grid[r1][c1]:
                        q.append(rw,cl)
                    else:
                        countAlt += 1
                     



        for r in range(rows):
            for c in range(cols):
                bfs(r,c)
            
        return result


S = Solution()
print(S.pacificAtlantic([[1,2,2,3,5],
                   [3,2,3,4,4],
                   [2,4,5,3,1],
                   [6,7,1,4,5],
                   [5,1,1,2,4]]
                   ))