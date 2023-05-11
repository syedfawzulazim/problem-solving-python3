from typing import List


class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        visited = set()
        adjacent = { i:[] for i in range(n)}

        for n1, n2 in edges:
            adjacent[n1].append(n2)
            adjacent[n2].append(n1)

        print(adjacent)

        def dfs(n, prev):
            if n in visited:
                return False
            visited.add(n)
            for x in adjacent[n]:
                if x == prev:
                    continue
                if not dfs(x, n):
                    return False
            return True

            
        
        return dfs(0,-1) and n == len(visited)




S = Solution()
S.valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])