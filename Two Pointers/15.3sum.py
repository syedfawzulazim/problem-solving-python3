from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        print(s)
        res = []
        l = 0
        r = len(s) -1
        while l + 1 < r:
            if s[l] + s[l+1] + s[r] < 0:
                l += 1
            elif s[l] + s[l+1] + s[r] > 0:
                r -= 1
            else:
                res.append([s[l], s[l+1], s[r]])
                l += 1
                r -= 1
        return res


S = Solution()
res = S.threeSum([-2, 0, 1, 1, 2])
print(res)