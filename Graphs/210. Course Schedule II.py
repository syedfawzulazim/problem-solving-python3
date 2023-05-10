from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        rows = len(prerequisites)

        for r in range(rows):
            preMap[prerequisites[r][0]].append(prerequisites[r][1])
        
        print(preMap)
        visited, cycle = set(), set()
        result = []
        def dfs(key):
            if key in cycle:
                return False
            if key in visited:
                return True
            
            cycle.add(key)

            for val in preMap[key]:
                if not dfs(val): return False

            cycle.remove(key)
            visited.add(key)
            result.append(key)

            return True
        
        for x in range(numCourses):
            if not dfs(x): return []
        return result





S = Solution()
r = S.findOrder(5, [[0,1],[0,2],[1,3],[1,4],[3,4]])
print(r)