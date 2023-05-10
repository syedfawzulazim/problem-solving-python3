from typing import List


class Solution:
    def connectionGraph3(self, n, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(n)]
        rank = [1] * n


        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return 
        

        for n1,n2 in edges:
            union(n1,n2)


        return len(set(par))


S = Solution()
print(S.connectionGraph3(5, [[0,1],[1,2],[3,4]]))