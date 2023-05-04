from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        
        def dfs(i):
            if sum(sol) == target:
                res.append(sol.copy())
                return
            if i >= len(candidates) or sum(sol) > target:
                return
            
            sol.append(candidates[i])
            dfs(i)
            sol.pop()
            dfs(i + 1)
          
        dfs(0)
        return res



S = Solution()
print(S.combinationSum([2,3,6,7], 7))