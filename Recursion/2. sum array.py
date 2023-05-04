from typing import List

class Solution:
    def recursion(self, nums:List, n: int, sum: int):
        if n >= len(nums):
            return sum
        sum += nums[n]
        x = self.recursion(nums, n+1, sum)
        a = 0
        a += 1
        return x
        

S = Solution()
x = S.recursion([1,2,3], 0, 0)
print(x)