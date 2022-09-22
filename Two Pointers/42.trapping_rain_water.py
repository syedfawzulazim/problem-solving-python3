from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = 1
        res = 0
        while l < len(height):
            if r >= len(height):
                l += 1
                r = l + 1
            if(r < len(height) and height[r] >= height[l]):
                j = l + 1
                while(j < r):
                    res += min(height[l], height[r]) - height[j]
                    j += 1
                l = r
                r = r + 1
            else:
                r += 1
        return res

S = Solution()
print(S.trap([4,2,3]))