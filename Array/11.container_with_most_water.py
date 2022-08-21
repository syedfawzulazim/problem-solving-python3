from typing import List

class Solution:
    def maxArea(self, col: List[int]) -> int:
        maxContainer = 0
        l = 0
        r = len(col) - 1
        dl = l + 1
        dr = r - 1
        maxContainer = min(col[l], col[r]) * (r-l)
        while dl < dr:
            if col[l+1] >= col[l] + dl - l:
                l += 1
                maxContainer = max(min(col[l], col[r]) * (r-l), maxContainer)
            dl = dl + 1
            if col[r-1] >= col[r] + r - dr:
                r -= 1
                maxContainer = max(min(col[l], col[r]) * (r-l), maxContainer)
            dr = dr - 1
            print(maxContainer)
        return maxContainer
           

S = Solution()
print(S.maxArea([2,3,4,5,18,17,6]))