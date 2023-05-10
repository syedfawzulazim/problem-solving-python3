from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        rows, cols = len(prerequisites), len(prerequisites[0])

        for r in range(rows):
            preMap[prerequisites[r][0]].append(prerequisites[r][1])
        
        print(preMap)
        visited = set()

        def dfs(key):
            if key in visited:
                return False
            if len(preMap[key]) == 0:
                return True
            visited.add(key)
            for val in preMap[key]:
                if not dfs(val): return False
            visited.remove(key)
            preMap[key] = []
            return True
        
        for x in range(numCourses):
            if not dfs(x): return False
        return True


S = Solution()
r = S.canFinish(5, [[0,1],[0,2],[1,3],[1,4],[3,4]])
print(r)