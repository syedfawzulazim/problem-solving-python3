from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        result = 0

        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(r, c, count):
            q = deque()
            q.append((r,c))

            while q:
                r1, c1 = q.popleft()
                visited.add((r1,c1))
                for r2, c2 in directions:
                    rw, cw = r1 + r2 , c1 + c2
                    if (rw in range(rows) 
                        and cw in range(cols) 
                        and (rw, cw ) not in visited
                        and grid[rw][cw] == 1
                        ):
                        count += 1
                        q.append((rw, cw))
                        visited.add((rw, cw))
            return count


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    result = max(result, bfs(r,c, 1))

        
        return result




S = Solution()
print(S.maxAreaOfIsland( [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    ))